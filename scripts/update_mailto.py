import glob

def replace_mailto():
    # Only legal files and maybe misc files
    files = glob.glob('pages/legal/*.html') + glob.glob('pages/misc/*.html')
    target_str = 'mailto:compliance@kensingtonivy.co.uk'
    
    for filepath in files:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        if target_str in content:
            # If in pages/misc, path should be ../legal/enquiry.html
            # If in pages/legal, path is enquiry.html
            replacement = 'enquiry.html' if 'pages/legal' in filepath else '../legal/enquiry.html'
            
            new_content = content.replace(target_str, replacement)
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Updated link in {filepath}")

if __name__ == '__main__':
    replace_mailto()
