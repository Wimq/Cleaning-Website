import os
import glob

def get_full_footer():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    start_tag = '<!-- FOOTER -->'
    end_tag = '</footer>'
    start_idx = content.find(start_tag)
    end_idx = content.find(end_tag, start_idx) + len(end_tag)
    
    footer = content[start_idx:end_idx]
    
    # Base adjustments (assuming depth of 1 level inside pages/ e.g. pages/legal/)
    footer = footer.replace('href="index.html"', 'href="../../index.html"')
    footer = footer.replace('href="/index.html"', 'href="../../index.html"')
    footer = footer.replace('href="pages/about.html"', 'href="../about.html"')
    footer = footer.replace('href="pages/faq/faq.html"', 'href="../faq/faq.html"')
    footer = footer.replace('href="pages/hire-staff.html"', 'href="../hire-staff.html"')
    
    # By default, make legal links relative to legal folder (for pages/legal/*.html)
    footer = footer.replace('href="pages/legal/privacy.html"', 'href="privacy.html"')
    footer = footer.replace('href="pages/legal/terms.html"', 'href="terms.html"')
    footer = footer.replace('href="pages/legal/cookies.html"', 'href="cookies.html"')
    
    return footer

def get_misc_footer(footer):
    # Adjust paths for pages in other subdirectories (misc, faq, courses)
    footer = footer.replace('href="privacy.html"', 'href="../legal/privacy.html"')
    footer = footer.replace('href="terms.html"', 'href="../legal/terms.html"')
    footer = footer.replace('href="cookies.html"', 'href="../legal/cookies.html"')
    return footer

def replace_footer(filepath, new_footer):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    start_tag = '<footer class="footer">'
    end_tag = '</footer>'
    start_idx = content.find(start_tag)
    if start_idx == -1:
        # Check if the footer tag is just <footer ...>
        start_tag = '<footer'
        start_idx = content.find(start_tag)
        if start_idx == -1:
            return
            
    end_idx = content.find(end_tag, start_idx) + len(end_tag)
    
    new_content = content[:start_idx] + new_footer + content[end_idx:]
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)

def main():
    legal_footer = get_full_footer()
    misc_footer = get_misc_footer(legal_footer)
    
    # Apply to all subdirectories
    subdirs = ['legal', 'misc', 'faq', 'courses']
    for subdir in subdirs:
        files = glob.glob(f'pages/{subdir}/*.html')
        footer_to_use = legal_footer if subdir == 'legal' else misc_footer
        for filepath in files:
            replace_footer(filepath, footer_to_use)

if __name__ == '__main__':
    main()
    print("Success: Updated footers for all subdirectories.")
