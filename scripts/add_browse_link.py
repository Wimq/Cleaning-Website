import os
import glob

# Add "Browse All Courses" to the Quick Links sidebar of each course page
old_quick_links = '''        <nav class="legal-nav-list">
            <a href="../register.html">Enquire Now</a>
            <a href="../faq/faq.html">FAQs</a>
            <a href="../hire-staff.html">Request Placement</a>
        </nav>'''

new_quick_links = '''        <nav class="legal-nav-list">
            <a href="../find-courses.html">Browse All Courses</a>
            <a href="../register.html">Enquire Now</a>
            <a href="../faq/faq.html">FAQs</a>
            <a href="../hire-staff.html">Request Placement</a>
        </nav>'''

course_dir = 'pages/courses'
for fname in os.listdir(course_dir):
    if not fname.endswith('.html'):
        continue
    fpath = os.path.join(course_dir, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if 'Browse All Courses' not in content:
        new_content = content.replace(old_quick_links, new_quick_links)
        if new_content != content:
            with open(fpath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f'Updated sidebar in: {fpath}')

print('Done.')
