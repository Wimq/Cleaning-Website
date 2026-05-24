import os

def update_kid_headers():
    files = [
        'pages/misc/kid.html',
        'pages/misc/kid-umbrella.html'
    ]
    
    old_header = '<div class="top-bar"><div class="container top-bar-inner"><div class="top-contact"><a href="tel:02074440009"><i data-lucide="phone"></i> 020 7444 0009</a></div><div class="top-links"><a href="../../index.html">← Back to Home</a></div></div></div>\n<header class="header"><div class="container header-inner"><a href="../../index.html" class="logo"><span class="logo-text">Kensington</span><span class="logo-accent">Ivy</span></a></div></header>'
    
    new_header = '''<header class="header">
    <div class="container header-inner">
        <a href="../../index.html" class="logo"><span class="logo-text">Kensington</span><span class="logo-accent">Ivy</span></a>
        <div class="header-cta">
            <a href="../legal/enquiry.html" class="btn btn-outline">Data Enquiry</a>
        </div>
    </div>
</header>'''

    for filepath in files:
        if os.path.exists(filepath):
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
                
            # Replace top bar and header
            content = content.replace(old_header, new_header)
            
            # Add Back to Home link in legal-hub-header if not present
            if '<h1>Key Information Document' in content and 'Back to Home' not in content.split('<div class="legal-hub-header">')[1][:200]:
                content = content.replace(
                    '        <h1>Key Information Document',
                    '        <a href="../../index.html" style="color: var(--gold); text-decoration: none; font-weight: 600; font-size: 0.9rem; margin-bottom: 1rem; display: inline-block;">&larr; Back to Home</a>\n        <h1>Key Information Document'
                )
                
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)

if __name__ == '__main__':
    update_kid_headers()
    print("Success")
