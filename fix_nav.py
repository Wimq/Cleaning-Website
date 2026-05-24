import os
import glob

workspace = "/Users/sharifafzal/untitled folder 10"
html_files = glob.glob(os.path.join(workspace, "**", "*.html"), recursive=True)

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content
    
    # Replace the duplicate University Registries pill with About Us
    content = content.replace(
        '<a href="pages/registries.html" class="sec-nav-pill"><i data-lucide="building-2" style="width: 16px;"></i> University Registries</a>',
        '<a href="pages/about.html" class="sec-nav-pill"><i data-lucide="info" style="width: 16px;"></i> About Us</a>'
    )
    content = content.replace(
        '<a href="registries.html" class="sec-nav-pill"><i data-lucide="building-2" style="width: 16px;"></i> University Registries</a>',
        '<a href="about.html" class="sec-nav-pill"><i data-lucide="info" style="width: 16px;"></i> About Us</a>'
    )
    content = content.replace(
        '<a href="../pages/registries.html" class="sec-nav-pill"><i data-lucide="building-2" style="width: 16px;"></i> University Registries</a>',
        '<a href="../pages/about.html" class="sec-nav-pill"><i data-lucide="info" style="width: 16px;"></i> About Us</a>'
    )
    # The one with ?v=3 in index.html is already updated

    if content != original:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated: {file}")
