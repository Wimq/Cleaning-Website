import os

def get_misc_footer():
    with open('index.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    start_tag = '<!-- FOOTER -->'
    end_tag = '</footer>'
    start_idx = content.find(start_tag)
    end_idx = content.find(end_tag, start_idx) + len(end_tag)
    footer = content[start_idx:end_idx]
    
    # Adjust paths since find-courses.html is 1 level deep inside pages/
    footer = footer.replace('href="index.html"', 'href="../index.html"')
    footer = footer.replace('href="/index.html"', 'href="../index.html"')
    footer = footer.replace('href="pages/about.html"', 'href="about.html"')
    footer = footer.replace('href="pages/faq/faq.html"', 'href="faq/faq.html"')
    footer = footer.replace('href="pages/hire-staff.html"', 'href="hire-staff.html"')
    footer = footer.replace('href="pages/legal/privacy.html"', 'href="legal/privacy.html"')
    footer = footer.replace('href="pages/legal/terms.html"', 'href="legal/terms.html"')
    footer = footer.replace('href="pages/legal/cookies.html"', 'href="legal/cookies.html"')
    return footer

filepath = 'pages/find-courses.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

new_footer = get_misc_footer()
content = content.replace('<footer class="footer"></footer>', new_footer)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Injected footer into find-courses.html")
