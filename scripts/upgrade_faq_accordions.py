import os
import glob
import re

def get_new_styles():
    return """
        .faq-hero {
            padding: 12rem 0 8rem 0;
            background: var(--navy);
            color: #fff;
        }
        .back-nav {
            display: flex;
            align-items: center;
            gap: 0.5rem;
            color: var(--gold);
            text-decoration: none;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.1em;
            font-size: 0.85rem;
            margin-bottom: 2rem;
            transition: var(--ease);
        }
        .back-nav:hover {
            transform: translateX(-5px);
        }
        
        .faq-list {
            max-width: 900px;
            margin: 6rem auto;
            counter-reset: faq-counter;
        }
        .faq-item {
            background: #fff;
            border: 1px solid rgba(0,0,0,0.05);
            border-radius: 16px;
            margin-bottom: 1.5rem;
            box-shadow: 0 10px 30px rgba(0,0,0,0.03);
            transition: all 0.4s ease;
            overflow: hidden;
        }
        .faq-item:hover {
            box-shadow: 0 15px 40px rgba(10, 17, 40, 0.08);
            border-color: rgba(201,162,88,0.3);
            transform: translateY(-2px);
        }
        .faq-item.active {
            border-color: var(--gold);
            box-shadow: 0 15px 40px rgba(201,162,88,0.15);
        }
        .faq-trigger {
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
        }
        .faq-trigger::before {
            counter-increment: faq-counter;
            content: "Q" counter(faq-counter);
            background: rgba(201,162,88,0.1);
            color: var(--gold);
            padding: 0.4rem 0.8rem;
            border-radius: 8px;
            font-size: 0.9rem;
            font-family: var(--ff-body);
            font-weight: 800;
        }
        .faq-trigger span {
            flex: 1;
            padding-left: 0.5rem;
        }
        .faq-trigger i {
            color: var(--gold);
            transition: transform 0.4s cubic-bezier(0.4, 0, 0.2, 1);
            background: rgba(201,162,88,0.05);
            border-radius: 50%;
            padding: 8px;
            width: 36px;
            height: 36px;
        }
        .faq-content {
            max-height: 0;
            overflow: hidden;
            transition: max-height 0.5s cubic-bezier(0.4, 0, 0.2, 1), opacity 0.5s ease;
            opacity: 0;
        }
        .faq-item.active .faq-content {
            max-height: 1000px;
            opacity: 1;
        }
        .faq-item.active .faq-trigger i {
            transform: rotate(180deg);
            background: var(--gold);
            color: #fff;
        }
        .faq-inner {
            min-height: 0;
            padding: 0 2rem 2rem 5rem;
            color: var(--muted);
            font-size: 1.1rem;
            line-height: 1.8;
        }
"""

def upgrade_accordions():
    files = [
        'pages/faq/faq.html',
        'pages/faq/faq-schools.html',
        'pages/faq/faq-compliance.html'
    ]
    
    for filepath in files:
        if os.path.exists(filepath):
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                
            # Find style block
            start_idx = content.find('<style>')
            end_idx = content.find('</style>', start_idx)
            
            if start_idx != -1 and end_idx != -1:
                new_content = content[:start_idx+7] + get_new_styles() + content[end_idx:]
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Upgraded {filepath}")

if __name__ == '__main__':
    upgrade_accordions()
