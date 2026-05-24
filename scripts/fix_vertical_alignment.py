import os
import glob
import re

def fix_vertical():
    faq_files = glob.glob('pages/faq/faq-*.html')
    for filepath in faq_files:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Update the trigger padding and add strict vertical centering
        content = content.replace(
            'padding: 1rem 1.5rem;',
            'padding: 1.25rem 1.5rem;'
        )
        
        # Enforce strict vertical centering on the text wrapper
        content = content.replace(
            '''        .faq-trigger span {
            flex: 1 1 0%;
            text-align: left;
            padding-left: 1rem;
            margin: 0;
        }''',
            '''        .faq-trigger span {
            flex: 1 1 0%;
            text-align: left;
            padding-left: 1rem;
            margin: 0;
            display: flex;
            align-items: center;
            transform: translateY(1px);
        }'''
        )
        
        # Enforce strict vertical centering on the chevron
        content = content.replace(
            '''        .faq-trigger i {
            flex-shrink: 0;
            color: var(--gold);
            transition: transform 0.4s cubic-bezier(0.4, 0, 0.2, 1);
            background: rgba(201,162,88,0.05);
            border-radius: 50%;
            padding: 8px;
            width: 36px;
            height: 36px;
        }''',
            '''        .faq-trigger i {
            flex-shrink: 0;
            color: var(--gold);
            transition: transform 0.4s cubic-bezier(0.4, 0, 0.2, 1);
            background: rgba(201,162,88,0.05);
            border-radius: 50%;
            width: 36px;
            height: 36px;
            display: flex;
            align-items: center;
            justify-content: center;
        }'''
        )

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed vertical alignment in {filepath}")

if __name__ == '__main__':
    fix_vertical()
