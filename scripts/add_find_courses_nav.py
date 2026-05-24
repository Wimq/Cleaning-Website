import os
import glob

# Add "Find Courses" to nav in pages/courses/*.html (2 levels deep)
courses_nav_old = '''            <a href="../faq/faq.html" style="color: var(--navy); font-weight: 500;">University Registries</a>
            <a href="../hire-staff.html" style="color: var(--navy); font-weight: 500;">Request Placement</a>
            <a href="../about.html" style="color: var(--navy); font-weight: 500;">About Us</a>'''

courses_nav_new = '''            <a href="../find-courses.html" style="color: var(--navy); font-weight: 500;">Find Courses</a>
            <a href="../faq/faq.html" style="color: var(--navy); font-weight: 500;">University Registries</a>
            <a href="../hire-staff.html" style="color: var(--navy); font-weight: 500;">Request Placement</a>
            <a href="../about.html" style="color: var(--navy); font-weight: 500;">About Us</a>'''

# Add "Find Courses" to nav in pages/faq/*.html and pages/hire-staff.html etc
faq_nav_old = '''            <a href="faq.html" style="color: var(--navy); font-weight: 500;">University Registries</a>
            <a href="../hire-staff.html" style="color: var(--navy); font-weight: 500;">Request Placement</a>
            <a href="../about.html" style="color: var(--navy); font-weight: 500;">About Us</a>'''

faq_nav_new = '''            <a href="../find-courses.html" style="color: var(--navy); font-weight: 500;">Find Courses</a>
            <a href="faq.html" style="color: var(--navy); font-weight: 500;">University Registries</a>
            <a href="../hire-staff.html" style="color: var(--navy); font-weight: 500;">Request Placement</a>
            <a href="../about.html" style="color: var(--navy); font-weight: 500;">About Us</a>'''

# pages/hire-staff.html and pages/about.html (1 level deep from pages/)
hire_nav_old = '''            <a href="faq/faq.html" style="color: var(--navy); font-weight: 500;">University Registries</a>
            <a href="hire-staff.html" style="color: var(--navy); font-weight: 500;">Request Placement</a>
            <a href="about.html" style="color: var(--navy); font-weight: 500;">About Us</a>'''

hire_nav_new = '''            <a href="find-courses.html" style="color: var(--navy); font-weight: 500;">Find Courses</a>
            <a href="faq/faq.html" style="color: var(--navy); font-weight: 500;">University Registries</a>
            <a href="hire-staff.html" style="color: var(--navy); font-weight: 500;">Request Placement</a>
            <a href="about.html" style="color: var(--navy); font-weight: 500;">About Us</a>'''

# find-courses.html itself
find_nav_old = '''            <a href="faq/faq.html" style="color: var(--navy); font-weight: 500;">University Registries</a>
            <a href="hire-staff.html" style="color: var(--navy); font-weight: 500;">Request Placement</a>
            <a href="about.html" style="color: var(--navy); font-weight: 500;">About Us</a>'''

# homepage index.html (root level)
home_nav_old = '''            <a href="pages/faq/faq.html" style="color: var(--navy); font-weight: 500;">University Registries</a>
            <a href="pages/hire-staff.html" style="color: var(--navy); font-weight: 500;">Request Placement</a>
            <a href="pages/about.html" style="color: var(--navy); font-weight: 500;">About Us</a>'''

home_nav_new = '''            <a href="pages/find-courses.html" style="color: var(--navy); font-weight: 500;">Find Courses</a>
            <a href="pages/faq/faq.html" style="color: var(--navy); font-weight: 500;">University Registries</a>
            <a href="pages/hire-staff.html" style="color: var(--navy); font-weight: 500;">Request Placement</a>
            <a href="pages/about.html" style="color: var(--navy); font-weight: 500;">About Us</a>'''

# responsive homepage
resp_nav_old = '''            <a href="../pages/faq/faq.html" style="color: var(--navy); font-weight: 500;">University Registries</a>
            <a href="../pages/hire-staff.html" style="color: var(--navy); font-weight: 500;">Request Placement</a>
            <a href="../pages/about.html" style="color: var(--navy); font-weight: 500;">About Us</a>'''

resp_nav_new = '''            <a href="../pages/find-courses.html" style="color: var(--navy); font-weight: 500;">Find Courses</a>
            <a href="../pages/faq/faq.html" style="color: var(--navy); font-weight: 500;">University Registries</a>
            <a href="../pages/hire-staff.html" style="color: var(--navy); font-weight: 500;">Request Placement</a>
            <a href="../pages/about.html" style="color: var(--navy); font-weight: 500;">About Us</a>'''

updated = 0

for root, dirs, files in os.walk('.'):
    if '.git' in root or '.gemini' in root:
        continue
    for fname in files:
        if not fname.endswith('.html'):
            continue
        fpath = os.path.join(root, fname)
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        new_content = content
        if 'find-courses.html' not in new_content:
            # Try each replacement
            for old, new in [
                (courses_nav_old, courses_nav_new),
                (faq_nav_old, faq_nav_new),
                (hire_nav_old, hire_nav_new),
                (find_nav_old, hire_nav_new),  # reuse pages-level nav for find-courses itself
                (home_nav_old, home_nav_new),
                (resp_nav_old, resp_nav_new),
            ]:
                if old in new_content:
                    new_content = new_content.replace(old, new, 1)
                    break
        
        if new_content != content:
            with open(fpath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f'Updated nav in: {fpath}')
            updated += 1

print(f'\nTotal files updated: {updated}')
