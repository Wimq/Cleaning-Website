import os
import glob
import re

workspace = "/Users/sharifafzal/untitled folder 10"
html_files = glob.glob(os.path.join(workspace, "**", "*.html"), recursive=True)

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content

    # 1. Remove the "Manage preferences" button line
    content = re.sub(
        r'\s*<button class="cookie-btn-settings"[^>]*>Manage preferences</button>\s*',
        '\n',
        content
    )

    # 2. Make cookie details always visible by adding 'expanded' class
    content = content.replace(
        '<div class="cookie-banner-details" id="cookieDetails">',
        '<div class="cookie-banner-details expanded" id="cookieDetails">'
    )

    if content != original:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated cookie banner in {file}")
