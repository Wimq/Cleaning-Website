import os
import glob
import re

def update_apply_now():
    # Find all HTML files recursively in the workspace
    html_files = []
    for root, dirs, files in os.walk('.'):
        if 'node_modules' in root or '.git' in root or '.gemini' in root:
            continue
        for file in files:
            if file.endswith('.html'):
                html_files.append(os.path.join(root, file))

    for filepath in html_files:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Replace standard instances of Apply Now
        if 'Apply Now' in content:
            new_content = content.replace('>Apply Now<', '>Enquire Now<')
            if new_content != content:
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Updated '{filepath}'")

if __name__ == '__main__':
    update_apply_now()
