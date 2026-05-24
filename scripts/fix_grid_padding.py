import os
import glob
import re

def fix_grid_padding():
    faq_files = glob.glob('pages/faq/faq-*.html')
    for filepath in faq_files:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Update .faq-inner
        content = content.replace(
            '''        .faq-inner {
            overflow: hidden;
            min-height: 0;
            padding: 0 2rem 2rem 5rem;
            color: var(--muted);
            font-size: 1.1rem;
            line-height: 1.8;
        }''',
            '''        .faq-inner {
            overflow: hidden;
            min-height: 0;
            padding: 0 2rem 0 5rem;
            color: var(--muted);
            font-size: 1.1rem;
            line-height: 1.8;
            transition: padding-bottom 0.42s cubic-bezier(0.4, 0, 0.2, 1);
        }'''
        )
        
        # Add the active padding rule
        if '.faq-item.active .faq-inner' not in content:
            content = content.replace(
                '''        .faq-item.active .faq-trigger i {''',
                '''        .faq-item.active .faq-inner {
            padding-bottom: 2rem;
        }
        .faq-item.active .faq-trigger i {'''
            )

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Fixed grid padding in {filepath}")

if __name__ == '__main__':
    fix_grid_padding()
