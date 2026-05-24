import os
import glob

workspace = "/Users/sharifafzal/untitled folder 10"
html_files = glob.glob(os.path.join(workspace, "**", "*.html"), recursive=True)

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content
    
    # Remove the duplicate Find Courses pill in the secondary nav
    # Wait, we can replace it with Contact Us pointing to register.html
    # but the user said "remove free assessment".
    # So we can just remove Find Courses from the secondary nav completely, 
    # making it perfectly centered with 3 items.
    
    content = content.replace(
        '<a href="pages/find-courses.html" class="sec-nav-pill"><i data-lucide="search" style="width: 16px;"></i> Find Courses</a>\n',
        ''
    )
    content = content.replace(
        '<a href="find-courses.html" class="sec-nav-pill"><i data-lucide="search" style="width: 16px;"></i> Find Courses</a>\n',
        ''
    )
    content = content.replace(
        '<a href="../pages/find-courses.html" class="sec-nav-pill"><i data-lucide="search" style="width: 16px;"></i> Find Courses</a>\n',
        ''
    )
    
    # without newline
    content = content.replace(
        '        <a href="pages/find-courses.html" class="sec-nav-pill"><i data-lucide="search" style="width: 16px;"></i> Find Courses</a>',
        ''
    )
    content = content.replace(
        '        <a href="find-courses.html" class="sec-nav-pill"><i data-lucide="search" style="width: 16px;"></i> Find Courses</a>',
        ''
    )
    content = content.replace(
        '        <a href="../pages/find-courses.html" class="sec-nav-pill"><i data-lucide="search" style="width: 16px;"></i> Find Courses</a>',
        ''
    )

    if content != original:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated: {file}")
