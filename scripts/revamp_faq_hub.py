import os

def revamp_faq_hub():
    filepath = 'pages/faq/faq.html'
    if not os.path.exists(filepath): return
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the CSS style block
    style_start = content.find('<style>')
    style_end = content.find('</style>', style_start) + len('</style>')
    
    new_style = """<style>
        :root {
            --cream: var(--white);
        }
        .faq-hero {
            padding: 8rem 0 16rem 0;
            background: var(--navy);
            color: #fff;
            text-align: center;
            position: relative;
        }
        .category-card {
            background: #fff;
            padding: 4rem 3rem;
            border-radius: 24px;
            border: 1px solid rgba(0,0,0,0.05);
            box-shadow: 0 20px 40px rgba(10, 17, 40, 0.08);
            text-decoration: none;
            transition: all 0.4s cubic-bezier(0.25, 1, 0.5, 1);
            display: flex;
            flex-direction: column;
            align-items: center;
            text-align: center;
            position: relative;
            overflow: hidden;
            z-index: 10;
        }
        .category-card::before {
            content: '';
            position: absolute;
            top: 0; left: 0; width: 100%; height: 6px;
            background: var(--gold);
            transform: scaleX(0);
            transform-origin: left;
            transition: transform 0.4s ease;
        }
        .category-card:hover {
            transform: translateY(-15px);
            box-shadow: 0 30px 60px rgba(10, 17, 40, 0.15);
        }
        .category-card:hover::before {
            transform: scaleX(1);
        }
        .category-card i {
            color: var(--gold);
            width: 54px;
            height: 54px;
            margin-bottom: 2rem;
            transition: transform 0.4s ease;
        }
        .category-card:hover i {
            transform: scale(1.1);
        }
        .category-card h2 {
            font-family: var(--ff-head);
            font-size: 1.8rem;
            color: var(--navy);
            margin-bottom: 1.2rem;
            font-weight: 700;
        }
        .category-card p {
            color: var(--muted);
            font-size: 1.05rem;
            line-height: 1.6;
        }
        .category-card .btn-arrow {
            margin-top: 2.5rem;
            width: 45px;
            height: 45px;
            background: rgba(201,162,88,0.1);
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            color: var(--gold);
            transition: all 0.3s ease;
        }
        .category-card:hover .btn-arrow {
            background: var(--gold);
            color: #fff;
        }
        .premium-grid {
            padding: 0 0 10rem 0; 
            background: var(--cream); 
            margin-top: -10rem;
        }
    </style>"""

    content = content[:style_start] + new_style + content[style_end:]

    # Fix the section padding and margin
    content = content.replace('<section style="padding: 10rem 0; background: var(--cream);">', '<section class="premium-grid">')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

if __name__ == '__main__':
    revamp_faq_hub()
