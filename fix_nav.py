import os
import glob

workspace = "/Users/sharifafzal/untitled folder 10"
html_files = glob.glob(os.path.join(workspace, "**", "*.html"), recursive=True)

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content
    
    # Remove the Free Assessment pill completely
    content = content.replace(
        '<a href="pages/register.html" class="sec-nav-pill"><i data-lucide="clipboard-check" style="width: 16px;"></i> Free Assessment</a>\n',
        ''
    )
    content = content.replace(
        '<a href="register.html" class="sec-nav-pill"><i data-lucide="clipboard-check" style="width: 16px;"></i> Free Assessment</a>\n',
        ''
    )
    content = content.replace(
        '<a href="../pages/register.html" class="sec-nav-pill"><i data-lucide="clipboard-check" style="width: 16px;"></i> Free Assessment</a>\n',
        ''
    )

    # In case there's no trailing newline
    content = content.replace(
        '        <a href="pages/register.html" class="sec-nav-pill"><i data-lucide="clipboard-check" style="width: 16px;"></i> Free Assessment</a>',
        ''
    )
    content = content.replace(
        '        <a href="register.html" class="sec-nav-pill"><i data-lucide="clipboard-check" style="width: 16px;"></i> Free Assessment</a>',
        ''
    )
    content = content.replace(
        '        <a href="../pages/register.html" class="sec-nav-pill"><i data-lucide="clipboard-check" style="width: 16px;"></i> Free Assessment</a>',
        ''
    )

    if content != original:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated: {file}")
