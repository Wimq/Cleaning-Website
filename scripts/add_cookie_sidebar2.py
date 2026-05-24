import os
import glob
import re

def update_sidebar(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # We only care about the first one (the legal sidebar), but it's safe to just replace the first instance
    # in the file. Oh wait, "Website Terms" is also in the footer.
    # The sidebar is within <nav class="legal-nav-list"> ... </nav>
    # Let's just look for:
    # <nav class="legal-nav-list">
    # ...
    # </nav>
    
    # Actually, we can just replace:
    # <a href="terms.html">Website Terms</a>
    # <a href="terms.html" class="active">Website Terms</a>
    # <a href="../legal/terms.html">Website Terms</a>
    # <a href="../legal/terms.html" class="active">Website Terms</a>
    # Only if it's NOT followed by Cookie Policy already.
    
    # Let's just do a string replace on all variations, and then clean up duplicates.
    is_misc = 'pages/misc/' in filepath
    is_courses = 'pages/courses/' in filepath
    
    cookie_link = '            <a href="cookies.html">Cookie Policy</a>\n'
    if is_misc or is_courses:
        cookie_link = '            <a href="../legal/cookies.html">Cookie Policy</a>\n'
        
    variations = [
        '            <a href="terms.html">Website Terms</a>\n',
        '            <a href="terms.html" class="active">Website Terms</a>\n',
        '            <a href="../legal/terms.html">Website Terms</a>\n',
        '            <a href="../legal/terms.html" class="active">Website Terms</a>\n',
        '            <a href="terms.html">Website Terms</a>\r\n',
        '            <a href="terms.html" class="active">Website Terms</a>\r\n',
        '            <a href="../legal/terms.html">Website Terms</a>\r\n',
        '            <a href="../legal/terms.html" class="active">Website Terms</a>\r\n'
    ]
    
    new_content = content
    for var in variations:
        if var in new_content:
            # We must be careful not to replace the footer links. The footer links are usually:
            # <a href="terms.html">Terms</a>
            # Our variations look for "Website Terms" so it won't hit the footer if the footer says "Terms".
            # Let's check footer. Footer says <a href="terms.html">Terms</a>. So we're safe.
            if "Cookie Policy" not in new_content.split(var)[1][:100]: # check if it's right after
                new_content = new_content.replace(var, var + cookie_link)

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
