import os

def rebuild():
    filepath = 'pages/faq/faq.html'
    content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>FAQ Center | KensingtonIvy</title>
    <link rel="stylesheet" href="../../css/base.css">
    <link rel="stylesheet" href="../../css/layout.css">
    <link rel="stylesheet" href="../../css/components.css">
    <link rel="stylesheet" href="../../css/legal.css">
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;600;700&family=Inter:wght@300;400;500;600;700&display=swap" rel="stylesheet">
    <script src="https://unpkg.com/lucide@latest"></script>
    <style>
        body { margin: 0; padding: 0; }
        .split-layout {
            display: flex;
            min-height: calc(100vh - 90px);
            flex-wrap: wrap;
        }
        .split-left {
            flex: 0 0 40%;
            background: var(--navy);
            color: #fff;
            padding: 8rem 4rem;
            display: flex;
            flex-direction: column;
            justify-content: center;
            position: relative;
        }
        .split-right {
            flex: 0 0 60%;
            background: var(--off, #faf9f6);
            padding: 6rem;
            display: flex;
            flex-direction: column;
            justify-content: center;
            gap: 2rem;
        }
        @media (max-width: 992px) {
            .split-left, .split-right {
                flex: 0 0 100%;
                padding: 5rem 2rem;
            }
        }
        .info-tag {
            color: var(--gold);
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.3em;
            display: block;
            margin-bottom: 2rem;
            font-size: 0.9rem;
        }
        .split-left h1 {
            font-family: var(--ff-head);
            font-size: clamp(3rem, 5vw, 4.5rem);
            margin-bottom: 1.5rem;
            line-height: 1.1;
            font-weight: 700;
        }
        .split-left p {
            font-size: 1.15rem;
            color: rgba(255,255,255,0.7);
            line-height: 1.6;
            font-weight: 300;
            max-width: 400px;
        }

        .category-bar {
            background: #fff;
            border: 1px solid rgba(0,0,0,0.05);
            border-radius: 20px;
            padding: 2.5rem;
            display: flex;
            align-items: center;
            gap: 2rem;
            text-decoration: none;
            color: var(--navy);
            box-shadow: 0 10px 30px rgba(0,0,0,0.03);
            transition: all 0.4s cubic-bezier(0.25, 1, 0.5, 1);
            position: relative;
            overflow: hidden;
        }
        .category-bar::before {
            content: '';
            position: absolute;
            top: 0; left: 0; width: 6px; height: 100%;
            background: var(--gold);
            transform: scaleY(0);
            transform-origin: bottom;
            transition: transform 0.4s ease;
        }
        .category-bar:hover {
            transform: translateX(-10px);
            box-shadow: 15px 25px 50px rgba(10, 17, 40, 0.08);
            border-color: rgba(201,162,88,0.2);
        }
        .category-bar:hover::before {
            transform: scaleY(1);
        }
        .bar-icon {
            background: rgba(201,162,88,0.1);
            color: var(--gold);
            width: 70px;
            height: 70px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            flex-shrink: 0;
            transition: all 0.4s ease;
        }
        .category-bar:hover .bar-icon {
            background: var(--gold);
            color: #fff;
            transform: scale(1.1) rotate(5deg);
        }
        .bar-content {
            flex: 1;
        }
        .bar-content h2 {
            font-family: var(--ff-head);
            font-size: 1.5rem;
            margin-bottom: 0.5rem;
            font-weight: 700;
        }
        .bar-content p {
            color: var(--muted);
            font-size: 0.95rem;
            line-height: 1.5;
            margin: 0;
        }
        .bar-arrow {
            color: var(--gold);
            transition: transform 0.3s ease;
        }
        .category-bar:hover .bar-arrow {
            transform: translateX(5px);
        }
        
        /* Reveal animations */
        .reveal {
            opacity: 0;
            transform: translateY(20px);
            transition: all 0.8s ease;
        }
        .reveal.active {
            opacity: 1;
            transform: translateY(0);
        }
    </style>
</head>
<body>

    <nav class="navbar"></nav> <!-- To be replaced by update_faq_headers.py -->

    <div class="split-layout">
        <div class="split-left">
            <span class="info-tag">Information Hub</span>
            <h1>How can we help?</h1>
            <p>Choose a category to explore detailed answers about our services, standards, and university pathways.</p>
        </div>
        <div class="split-right">
            
            <a href="faq-schools.html" class="category-bar reveal" style="transition-delay: 0.1s;">
                <div class="bar-icon"><i data-lucide="school" style="width: 32px; height: 32px;"></i></div>
                <div class="bar-content">
                    <h2>For Universities & Partners</h2>
                    <p>Guidance on student quality, partnership agreements, clearing cycles, and placement coordination.</p>
                </div>
                <div class="bar-arrow"><i data-lucide="arrow-right"></i></div>
            </a>

            <a href="faq.html" class="category-bar reveal" style="transition-delay: 0.2s;">
                <div class="bar-icon"><i data-lucide="graduation-cap" style="width: 32px; height: 32px;"></i></div>
                <div class="bar-content">
                    <h2>For Students & Applicants</h2>
                    <p>Everything about qualifications, UCAS tariff requirements, clearing advisory, and entry pathways.</p>
                </div>
                <div class="bar-arrow"><i data-lucide="arrow-right"></i></div>
            </a>

            <a href="faq-compliance.html" class="category-bar reveal" style="transition-delay: 0.3s;">
                <div class="bar-icon"><i data-lucide="shield-check" style="width: 32px; height: 32px;"></i></div>
                <div class="bar-content">
                    <h2>Admissions Standards & Compliance</h2>
                    <p>Detailed insight into qualification verification, background screening, and Student Finance support.</p>
                </div>
                <div class="bar-arrow"><i data-lucide="arrow-right"></i></div>
            </a>

        </div>
    </div>

    <footer class="footer"></footer> <!-- To be replaced by update_footers.py -->

    <script>
        lucide.createIcons();
        const revealElements = document.querySelectorAll('.reveal');
        setTimeout(() => {
            revealElements.forEach(el => el.classList.add('active'));
        }, 100);
    </script>
</body>
</html>
"""
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == '__main__':
    rebuild()
