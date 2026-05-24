import os
import glob

def replace_email():
    target = 'contact@kensingtonivy.co.uk'
    # Assuming user made a typo with "enquires", substituting with "enquiries"
    replacement = 'enquiries@kensingtonivy.co.uk'
    
    html_files = []
    for root, dirs, files in os.walk('.'):
        for file in files:
            if file.endswith('.html'):
                html_files.append(os.path.join(root, file))
                
    count = 0
    for filepath in html_files:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        if target in content:
            new_content = content.replace(target, replacement)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated {filepath}")
            count += 1
            
    print(f"Replaced {target} with {replacement} in {count} files.")

if __name__ == '__main__':
    replace_email()
