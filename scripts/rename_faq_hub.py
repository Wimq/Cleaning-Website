import os

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    new_content = content.replace('>FAQ Hub<', '>Help Center<')

    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filepath}")

for root, _, files in os.walk('.'):
    for file in files:
        if file.endswith('.html') or file.endswith('.py'):
            if file == 'rename_faq_hub.py': continue
            process_file(os.path.join(root, file))

print("Done")
