import os
import glob
import re

workspace = "/Users/sharifafzal/untitled folder 10"
html_files = glob.glob(os.path.join(workspace, "**", "*.html"), recursive=True)

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content
    
    # Strip everything from <!-- Floating Cookie Button --> to </body>
    content = re.sub(r'<!-- Floating Cookie Button -->.*?</body>', '</body>', content, flags=re.DOTALL)
    
    if content != original:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Stripped v4 widgets from {file}")
