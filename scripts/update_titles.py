import os
import glob
import re

html_files = glob.glob('**/*.html', recursive=True)

for filepath in html_files:
    if os.path.isfile(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Replace occurrences of "Kensington Ivy Ltd</title>" with "KensingtonIvy</title>"
        new_content = re.sub(r'Kensington\s+Ivy\s+Ltd</title>', 'KensingtonIvy</title>', content, flags=re.IGNORECASE)
        # Also catch just "Kensington Ivy</title>" just in case
        new_content = re.sub(r'Kensington\s+Ivy</title>', 'KensingtonIvy</title>', new_content, flags=re.IGNORECASE)
        
        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)

print("Title tags updated successfully.")
