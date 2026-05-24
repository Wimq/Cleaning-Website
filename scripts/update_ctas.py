import os
import re

directory = 'pages/legal'
files_to_update = [
    'privacy.html',
    'terms.html',
    'cookies.html',
    'safeguarding.html',
    'accessibility.html',
    'modern-slavery.html',
    'social-value.html'
]

for filename in files_to_update:
    filepath = os.path.join(directory, filename)
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Regex to find <div class="header-cta"> ... </div>
        # Use dotall to match across newlines
        pattern = re.compile(r'<div class="header-cta">\s*<a href="[^"]+" class="btn btn-outline">[^<]+</a>\s*</div>', re.DOTALL)
        
        # In terms.html it might be slightly different or missing the href/class? Let's check.
        # It's safer to just replace any <div class="header-cta">...</div> that contains a btn-outline
        
        # More robust replacement
        new_cta = '<div class="header-cta">\n            <a href="enquiry.html" class="btn btn-outline">Data Enquiry</a>\n        </div>'
        
        content = re.sub(r'<div class="header-cta">.*?</div>', new_cta, content, flags=re.DOTALL)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
            
print("Success")
