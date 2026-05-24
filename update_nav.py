import os
import glob

workspace = "/Users/sharifafzal/untitled folder 10"

html_files = glob.glob(os.path.join(workspace, "**", "*.html"), recursive=True)

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    original = content
    
    # 1. Replace Oxbridge & Elite in secondary nav
    content = content.replace(
        '<a href="pages/oxbridge-elite.html" class="sec-nav-pill"><i data-lucide="award" style="width: 16px;"></i> Oxbridge & Elite</a>',
        '<a href="pages/reviews.html" class="sec-nav-pill"><i data-lucide="star" style="width: 16px;"></i> Reviews</a>'
    )
    content = content.replace(
        '<a href="oxbridge-elite.html" class="sec-nav-pill"><i data-lucide="award" style="width: 16px;"></i> Oxbridge & Elite</a>',
        '<a href="reviews.html" class="sec-nav-pill"><i data-lucide="star" style="width: 16px;"></i> Reviews</a>'
    )
    content = content.replace(
        '<a href="../oxbridge-elite.html" class="sec-nav-pill"><i data-lucide="award" style="width: 16px;"></i> Oxbridge & Elite</a>',
        '<a href="../reviews.html" class="sec-nav-pill"><i data-lucide="star" style="width: 16px;"></i> Reviews</a>'
    )

    # 2. Replace Request Placement in top links
    # Pattern 1: pages/hire-staff.html
    content = content.replace(
        '<a href="pages/hire-staff.html" style="color: var(--navy); font-weight: 500;">Request Placement</a>',
        '<a href="pages/foundation-years.html" style="color: var(--navy); font-weight: 500;">Foundation Years</a>'
    )
    # Pattern 2: hire-staff.html
    content = content.replace(
        '<a href="hire-staff.html" style="color: var(--navy); font-weight: 500;">Request Placement</a>',
        '<a href="foundation-years.html" style="color: var(--navy); font-weight: 500;">Foundation Years</a>'
    )
    # Pattern 3: ../hire-staff.html
    content = content.replace(
        '<a href="../hire-staff.html" style="color: var(--navy); font-weight: 500;">Request Placement</a>',
        '<a href="../foundation-years.html" style="color: var(--navy); font-weight: 500;">Foundation Years</a>'
    )
    
    # Also handle the footer replacements for hire-staff.html
    content = content.replace(
        '<a href="pages/hire-staff.html" style="color: rgba(255,255,255,0.7); font-size: 1rem; transition: var(--ease);">Request Placement</a>',
        '<a href="pages/foundation-years.html" style="color: rgba(255,255,255,0.7); font-size: 1rem; transition: var(--ease);">Foundation Years</a>'
    )
    content = content.replace(
        '<a href="hire-staff.html" style="color: rgba(255,255,255,0.7); font-size: 1rem; transition: var(--ease);">Request Placement</a>',
        '<a href="foundation-years.html" style="color: rgba(255,255,255,0.7); font-size: 1rem; transition: var(--ease);">Foundation Years</a>'
    )
    content = content.replace(
        '<a href="../hire-staff.html" style="color: rgba(255,255,255,0.7); font-size: 1rem; transition: var(--ease);">Request Placement</a>',
        '<a href="../foundation-years.html" style="color: rgba(255,255,255,0.7); font-size: 1rem; transition: var(--ease);">Foundation Years</a>'
    )

    if content != original:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated: {file}")
