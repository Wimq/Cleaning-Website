import os
import re

def process_file(filepath):
    if not os.path.exists(filepath): return
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Extract h1
    h1_match = re.search(r'<h1[^>]*>(.*?)</h1>', content, re.DOTALL)
    h1_text = h1_match.group(1).strip() if h1_match else "FAQ"

    # Extract p in hero
    p_match = re.search(r'<p[^>]*max-width[^>]*>(.*?)</p>', content, re.DOTALL)
    p_text = p_match.group(1).strip() if p_match else ""

    # Extract faq-list
    list_start = content.find('<div class="faq-list">')
    if list_start == -1: return
    # Find matching closing div
    open_divs = 0
    list_end = -1
    i = list_start
    while i < len(content):
        if content[i:i+4] == '<div':
            open_divs += 1
            i += 4
        elif content[i:i+5] == '</div':
            open_divs -= 1
            if open_divs == 0:
                list_end = i + 6
                break
            i += 5
        else:
            i += 1
            
    faq_list_content = content[list_start:list_end] if list_end != -1 else ""
    # Remove the inline margin/max-width from faq-list
    faq_list_content = re.sub(r'class="faq-list"[^>]*', 'class="faq-list" style="margin: 0 auto; max-width: 850px; width: 100%;"', faq_list_content, 1)

    new_html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{h1_text} | KensingtonIvy FAQ</title>
    <link rel="stylesheet" href="../../css/base.css">
    <link rel="stylesheet" href="../../css/layout.css">
    <link rel="stylesheet" href="../../css/components.css">
    <link rel="stylesheet" href="../../css/legal.css">
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;600;700&family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <script src="https://unpkg.com/lucide@latest"></script>
    <style>
        body {{ margin: 0; padding: 0; }}
        .split-layout {{
            display: flex;
            flex-wrap: wrap;
            align-items: flex-start;
        }}
        .split-left {{
            flex: 0 0 40%;
            background: var(--navy);
            color: #fff;
            padding: 8rem 4rem;
            display: flex;
            flex-direction: column;
            justify-content: center;
            position: sticky;
            top: 0;
            height: 100vh;
        }}
        .split-right {{
            flex: 0 0 60%;
            background: var(--off, #faf9f6);
            padding: 8rem 6rem;
            display: flex;
            flex-direction: column;
            min-height: 100vh;
        }}
        @media (max-width: 992px) {{
            .split-left {{
                position: relative;
                height: auto;
                padding: 6rem 2rem 4rem 2rem;
            }}
            .split-left, .split-right {{
                flex: 0 0 100%;
                padding: 4rem 2rem;
            }}
        }}
        
        .back-nav {{
            display: inline-flex;
            align-items: center;
            gap: 0.5rem;
            color: var(--gold);
            text-decoration: none;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.1em;
            font-size: 0.85rem;
            margin-bottom: 3rem;
            transition: var(--ease);
        }}
        .back-nav:hover {{
            transform: translateX(-5px);
        }}

        .split-left h1 {{
            font-family: var(--ff-head);
            font-size: clamp(3rem, 5vw, 4rem);
            margin-bottom: 1.5rem;
            line-height: 1.1;
            font-weight: 700;
        }}
        .split-left p {{
            font-size: 1.15rem;
            color: rgba(255,255,255,0.7);
            line-height: 1.6;
            font-weight: 300;
            max-width: 400px;
        }}

        /* Premium Accordion Styles */
        .faq-list {{
            counter-reset: faq-counter;
        }}
        .faq-item {{
            background: #fff;
            border: 1px solid rgba(0,0,0,0.05);
            border-radius: 16px;
            margin-bottom: 1.5rem;
            box-shadow: 0 10px 30px rgba(0,0,0,0.03);
            transition: all 0.4s ease;
            overflow: hidden;
        }}
        .faq-item:hover {{
            box-shadow: 0 15px 40px rgba(10, 17, 40, 0.08);
            border-color: rgba(201,162,88,0.3);
            transform: translateY(-2px);
        }}
        .faq-item.active {{
            border-color: var(--gold);
            box-shadow: 0 15px 40px rgba(201,162,88,0.15);
        }}
        .faq-trigger {{
            width: 100%;
            padding: 1.25rem 1.5rem;
            display: flex;
            justify-content: flex-start;
            align-items: center;
            gap: 1rem;
            background: none;
            border: none;
            cursor: pointer;
            text-align: left;
            font-family: var(--ff-body);
            font-size: 1.05rem;
            line-height: 1.4;
            color: var(--navy);
            font-weight: 600;
            transition: var(--ease);
        }}
        .faq-trigger::before {{
            counter-increment: faq-counter;
            content: "Q" counter(faq-counter);
            background: rgba(201,162,88,0.1);
            color: var(--gold);
            padding: 0.4rem 0.8rem;
            border-radius: 8px;
            font-size: 0.9rem;
            font-family: var(--ff-body);
            font-weight: 800;
        }}
        .faq-trigger span {{
            flex: 1;
            padding-left: 0.5rem;
        }}
        .faq-trigger i {{
            color: var(--gold);
            transition: transform 0.4s cubic-bezier(0.4, 0, 0.2, 1);
            background: rgba(201,162,88,0.05);
            border-radius: 50%;
            padding: 8px;
            width: 36px;
            height: 36px;
        }}
        .faq-content {{
            max-height: 0;
            overflow: hidden;
            transition: max-height 0.5s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.5s ease;
            opacity: 0;
        }}
        .faq-item.active .faq-content {{
            max-height: 1000px;
            opacity: 1;
        }}
        .faq-item.active .faq-trigger i {{
            transform: rotate(180deg);
            background: var(--gold);
            color: #fff;
        }}
        .faq-inner {{
            min-height: 0;
            padding: 0 2rem 2rem 5rem;
            color: var(--muted);
            font-size: 1.1rem;
            line-height: 1.8;
        }}
    </style>
</head>
<body>

    <nav class="navbar"></nav> <!-- To be replaced by update_faq_headers.py -->

    <div class="split-layout">
        <div class="split-left">
            <a href="faq.html" class="back-nav">
                <i data-lucide="arrow-left" style="width: 16px;"></i>
                Back to Center
            </a>
            <h1>{h1_text}</h1>
            <p>{p_text}</p>
        </div>
        <div class="split-right">
            {faq_list_content}
        </div>
    </div>

    <footer class="footer"></footer> <!-- To be replaced by update_footers.py -->

    <script>
        lucide.createIcons();

        // FAQ Accordion Logic
        const faqTriggers = document.querySelectorAll('.faq-trigger');
        faqTriggers.forEach(trigger => {{
            trigger.addEventListener('click', () => {{
                const parent = trigger.parentElement;
                
                // Close others
                document.querySelectorAll('.faq-item').forEach(item => {{
                    if (item !== parent) item.classList.remove('active');
                }});
                
                // Toggle current
                parent.classList.toggle('active');
            }});
        }});
    </script>
</body>
</html>
"""
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_html)
    print(f"Rebuilt {filepath}")

for f in ['pages/faq/faq.html', 'pages/faq/faq-schools.html', 'pages/faq/faq-compliance.html']:
    process_file(f)
