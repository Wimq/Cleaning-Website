import os
import glob
import re

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # We need to find hrefs to faq-educators.html that have the text "Placement FAQs"
    # Example 1: <a href="../faq/faq-educators.html" ...>Placement FAQs</a>
    # Example 2: <a href="pages/faq/faq-educators.html" ...>Placement FAQs</a>
    # Example 3: <a href="faq-educators.html" ...>Placement FAQs</a>
    
    # Let's replace the text first
    new_content = content.replace('>Placement FAQs<', '>Help Center<')
    
    # Now replace the hrefs specifically for the FAQ link
    new_content = new_content.replace('faq/faq-educators.html', 'faq/faq.html')
    new_content = new_content.replace('"faq-educators.html"', '"faq.html"')

    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filepath}")

for root, _, files in os.walk('.'):
    for file in files:
        if file.endswith('.html') or file.endswith('.py'):
            if file == 'replace_placement_faq.py': continue
            process_file(os.path.join(root, file))

print("Done")
