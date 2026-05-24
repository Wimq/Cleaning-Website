import os
import glob
import re

def rewrite_css(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Define the new CSS block
    new_css = '''        .faq-trigger {
            width: 100%;
            padding: 1rem 1.5rem;
            display: flex;
            align-items: center;
            justify-content: space-between;
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
            padding: 0.4rem 0;
            border-radius: 8px;
            font-size: 0.9rem;
            font-family: var(--ff-body);
            font-weight: 800;
            flex-shrink: 0;
            width: 3rem;
            display: flex;
            justify-content: center;
            align-items: center;
        }
        .faq-trigger span {
            flex: 1 1 0%;
            text-align: left;
            padding-left: 1rem;
            margin: 0;
        }
        .faq-trigger i {
            flex-shrink: 0;
            color: var(--gold);
            transition: transform 0.4s cubic-bezier(0.4, 0, 0.2, 1);
            background: rgba(201,162,88,0.05);
            border-radius: 50%;
            padding: 8px;
            width: 36px;
            height: 36px;
        }'''

    # Extract everything from .faq-trigger { up to .faq-content {
    match = re.search(r'(\.faq-trigger\s*\{.*?\})(.+?)(\.faq-content\s*\{)', content, re.DOTALL)
    if match:
        content = content[:match.start(1)] + new_css + "\n" + content[match.start(3):]
    else:
        print(f"Warning: Couldn't find CSS block in {filepath}")
    
    # Strip the inline styles from span
    content = content.replace('<span style="text-align: left !important; flex-grow: 1; margin-left: 1.5rem;">', '<span>')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Fixed structural layout in {filepath}")

if __name__ == '__main__':
    faq_files = glob.glob('pages/faq/faq-*.html')
    for filepath in faq_files:
        rewrite_css(filepath)
