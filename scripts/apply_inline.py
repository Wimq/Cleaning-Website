import os
import glob
import re

def update_inline():
    faq_files = glob.glob('pages/faq/faq-*.html')
    for filepath in faq_files:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Replace <span> with <span style="text-align: left !important; flex-grow: 1; margin-left: 1.5rem;">
        # But handle cases where it might already be applied or have other attributes
        content = re.sub(r'<span(?!\s+style=)>', '<span style="text-align: left !important; flex-grow: 1; margin-left: 1.5rem;">', content)
        
        # Also let's make sure the inline style inside the head is !important
        content = content.replace('text-align: left;', 'text-align: left !important;')
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated inline styles in {filepath}")

if __name__ == '__main__':
    update_inline()
