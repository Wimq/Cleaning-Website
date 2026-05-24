import os
import glob

workspace = "/Users/sharifafzal/untitled folder 10"
html_files = glob.glob(os.path.join(workspace, "**", "*.html"), recursive=True)

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content
    content = content.replace('> Admissions FAQs</a>', '> FAQ</a>')
    content = content.replace('>Admissions FAQs</a>', '>FAQ</a>')

    if content != original:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated FAQ pill in {file}")
