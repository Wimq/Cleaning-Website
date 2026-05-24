import os
import glob

# 1. Update faq.html
faq_main = "pages/faq/faq.html"
if os.path.exists(faq_main):
    with open(faq_main, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Change title
    content = content.replace("<title>FAQ Center | KensingtonIvy</title>", "<title>Help Center | KensingtonIvy</title>")
    content = content.replace("FAQ Hub", "Information Center")
    
    # Fix self-link
    content = content.replace('href="faq.html" class="category-bar reveal" style="transition-delay: 0.2s;"', 'href="faq-educators.html" class="category-bar reveal" style="transition-delay: 0.2s;"')
    
    with open(faq_main, 'w', encoding='utf-8') as f:
        f.write(content)

# 2. Update subpages
subpages = ["pages/faq/faq-schools.html", "pages/faq/faq-educators.html", "pages/faq/faq-compliance.html"]
for page in subpages:
    if os.path.exists(page):
        with open(page, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Change title
        content = content.replace(" | KensingtonIvy FAQ</title>", " | KensingtonIvy Help Center</title>")
        
        # Center the text in the accordion
        if '.faq-trigger span {' in content:
            content = content.replace(
                '.faq-trigger span {\n            flex: 1;\n            padding-left: 0.5rem;\n        }',
                '.faq-trigger span {\n            flex: 1;\n            padding: 0 1rem;\n            text-align: center;\n        }'
            )
            
        # Update the max-width
        content = content.replace(
            'class="faq-list" style="margin: 0 auto; max-width: 850px; width: 100%;"',
            'class="faq-list" style="margin: 0 auto; max-width: 700px; width: 100%;"'
        )
        content = content.replace(
            'class="faq-list"',
            'class="faq-list" style="margin: 0 auto; max-width: 700px; width: 100%;"'
        )
        # Fix double application if there was one
        content = content.replace(
            'class="faq-list" style="margin: 0 auto; max-width: 700px; width: 100%;" style="margin: 0 auto; max-width: 700px; width: 100%;"',
            'class="faq-list" style="margin: 0 auto; max-width: 700px; width: 100%;"'
        )

        with open(page, 'w', encoding='utf-8') as f:
            f.write(content)

print("FAQ files updated.")
