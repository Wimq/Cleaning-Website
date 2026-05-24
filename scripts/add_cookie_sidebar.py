import os
import glob

def update_sidebar(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Depending on whether the file is in pages/legal/ or pages/misc/
    is_misc = 'pages/misc/' in filepath
    is_courses = 'pages/courses/' in filepath
    
    cookie_link = '<a href="cookies.html">Cookie Policy</a>'
    if is_misc or is_courses:
        cookie_link = '<a href="../legal/cookies.html">Cookie Policy</a>'
        
    # Find the Legal Hub sidebar. We look for the terms link and add cookie link after it.
    # In pages/legal: <a href="terms.html">Website Terms</a>
    # In pages/misc: <a href="../legal/terms.html">Website Terms</a>
    
    # We want to make sure we don't add it twice.
    if "Cookie Policy" in content and ("cookies.html" in content) and ('class="legal-nav-list"' in content):
        # wait, cookie policy might be in the footer. 
        pass
    
    # Let's find the exact block:
    # <nav class="legal-nav-list">
    #     <a href="privacy.html">...
    #     <a href="terms.html">Website Terms</a>
    
    terms_pattern_legal = '<a href="terms.html">Website Terms</a>\n'
    terms_pattern_legal_active = '<a href="terms.html" class="active">Website Terms</a>\n'
    terms_pattern_misc = '<a href="../legal/terms.html">Website Terms</a>\n'
    
    new_content = content
    if terms_pattern_legal in new_content:
        # Check if cookie link is already immediately after
        if cookie_link not in new_content:
            new_content = new_content.replace(terms_pattern_legal, terms_pattern_legal + f'            {cookie_link}\n')
    elif terms_pattern_legal_active in new_content:
        if cookie_link not in new_content:
            new_content = new_content.replace(terms_pattern_legal_active, terms_pattern_legal_active + f'            {cookie_link}\n')
    elif terms_pattern_misc in new_content:
         if cookie_link not in new_content:
            new_content = new_content.replace(terms_pattern_misc, terms_pattern_misc + f'            {cookie_link}\n')

    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {filepath}")

def main():
    files = glob.glob('pages/legal/*.html') + glob.glob('pages/misc/*.html') + glob.glob('pages/courses/*.html')
    for f in files:
        update_sidebar(f)

if __name__ == '__main__':
    main()
