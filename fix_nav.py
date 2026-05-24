import os
import glob

workspace = "/Users/sharifafzal/untitled folder 10"
html_files = glob.glob(os.path.join(workspace, "**", "*.html"), recursive=True)

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content
    
    # Replace the duplicate About Us pill with Free Assessment
    content = content.replace(
        '<a href="pages/about.html" class="sec-nav-pill"><i data-lucide="info" style="width: 16px;"></i> About Us</a>',
        '<a href="pages/register.html" class="sec-nav-pill"><i data-lucide="clipboard-check" style="width: 16px;"></i> Free Assessment</a>'
    )
    content = content.replace(
        '<a href="about.html" class="sec-nav-pill"><i data-lucide="info" style="width: 16px;"></i> About Us</a>',
        '<a href="register.html" class="sec-nav-pill"><i data-lucide="clipboard-check" style="width: 16px;"></i> Free Assessment</a>'
    )
    content = content.replace(
        '<a href="../pages/about.html" class="sec-nav-pill"><i data-lucide="info" style="width: 16px;"></i> About Us</a>',
        '<a href="../pages/register.html" class="sec-nav-pill"><i data-lucide="clipboard-check" style="width: 16px;"></i> Free Assessment</a>'
    )
    
    # Also handle the ?v=3 version just in case
    content = content.replace(
        '<a href="pages/about.html?v=3" class="sec-nav-pill"><i data-lucide="info" style="width: 16px;"></i> About Us</a>',
        '<a href="pages/register.html" class="sec-nav-pill"><i data-lucide="clipboard-check" style="width: 16px;"></i> Free Assessment</a>'
    )
    content = content.replace(
        '<a href="../pages/about.html?v=3" class="sec-nav-pill"><i data-lucide="info" style="width: 16px;"></i> About Us</a>',
        '<a href="../pages/register.html" class="sec-nav-pill"><i data-lucide="clipboard-check" style="width: 16px;"></i> Free Assessment</a>'
    )

    if content != original:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated: {file}")
