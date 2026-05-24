import os

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Fix the inline style
    new_content = content.replace('class="faq-list" style="margin: 0; max-width: none;"', 'class="faq-list" style="margin: 0 auto; max-width: 850px; width: 100%;"')

    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Fixed horizontal width in {filepath}")

for f in ['pages/faq/faq.html', 'pages/faq/faq-schools.html', 'pages/faq/faq-compliance.html', 'pages/faq/faq-educators.html']:
    if os.path.exists(f):
        process_file(f)

# Also fix rebuild_faq_subpages.py so it doesn't overwrite it
rebuild_file = 'rebuild_faq_subpages.py'
if os.path.exists(rebuild_file):
    with open(rebuild_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    new_content = content.replace("'class=\"faq-list\" style=\"margin: 0; max-width: none;\"'", "'class=\"faq-list\" style=\"margin: 0 auto; max-width: 850px; width: 100%;\"'")
    
    if new_content != content:
        with open(rebuild_file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print("Fixed rebuild_faq_subpages.py")
