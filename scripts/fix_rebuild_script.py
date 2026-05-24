import os

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    old_css = """        .faq-trigger {{
            width: 100%;
            padding: 2rem;
            display: flex;
            justify-content: flex-start;
            align-items: center;
            gap: 1rem;
            background: none;
            border: none;
            cursor: pointer;
            text-align: left;
            font-family: var(--ff-head);
            font-size: 1.4rem;
            color: var(--navy);
            font-weight: 700;
            transition: var(--ease);
        }}"""

    new_css = """        .faq-trigger {{
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
        }}"""

    new_content = content.replace(old_css, new_css)
    
    old_span = """        .faq-trigger span {{
            flex: 1;
            padding-left: 0.5rem;
        }}"""
    new_span = """        .faq-trigger span {{
            flex: 1;
            padding-left: 0.5rem;
        }}"""
        
    new_content = new_content.replace(old_span, new_span)

    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Fixed {filepath}")

process_file('rebuild_faq_subpages.py')
