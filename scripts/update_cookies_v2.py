import re

def update_cookies_file():
    filepath = "pages/legal/cookies.html"
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update Section 2 to add consent log retention
    target_2_4 = '<p>2.4. We maintain a secure, pseudonymised audit log of all consent obtained, including the timestamp, the consent version presented, and the specific categories consented to, to demonstrate compliance under the accountability principle (Article 5(2) UK GDPR).</p>'
    replacement_2_4 = '<p>2.4. <strong>Consent Record Retention:</strong> We maintain a secure, pseudonymised audit log of all consent obtained (capturing your anonymised IP address, user agent, timestamp, and the specific categories consented to). This is retained strictly to demonstrate compliance under the accountability principle (Article 5(2) UK GDPR). We retain these consent records for a maximum of 3 years following the withdrawal or expiration of your consent.</p>'
    content = content.replace(target_2_4, replacement_2_4)

    # 2. Add Age Appropriate Design Code & Profiling into Section 3
    target_3_1 = '<p>3.1. We categorise the cookies used on our Website strictly into four groups based on their function and purpose.</p>'
    replacement_3_1 = """<p>3.1. We categorise the cookies used on our Website strictly into four groups based on their function and purpose.</p>
        <p>3.2. <strong>Children's Data (Age Appropriate Design Code):</strong> As our services relate to higher education, our Website may be accessed by prospective students under the age of 18 (e.g., 16 or 17-year-olds). In strict compliance with the ICO's Age Appropriate Design Code, all non-essential tracking and profiling cookies are switched <strong>OFF by default</strong>. We do not employ "nudge techniques" to encourage children to activate tracking.</p>
        <p>3.3. <strong>Profiling and Automated Decision-Making:</strong> While our Marketing &amp; Targeting cookies (such as the Meta Pixel) are used to build advertising profiles, they are <strong>not</strong> used for automated decision-making that produces legal or similarly significant effects concerning you (Article 22 UK GDPR). They are used solely to present relevant recruitment opportunities.</p>"""
    content = content.replace(target_3_1, replacement_3_1)
    
    # 3. Update Section 7 to add note about Local Storage / Cache
    target_7_2 = '<p>7.2. <strong>Browser-Level Blocking and Deletion:</strong> Beyond our CMP, you can manage cookies comprehensively at the browser level. If you wish to delete all cookies currently stored on your device, or configure your browser to block third-party cookies globally, please follow the specific instructions provided by your browser manufacturer:</p>'
    replacement_7_2 = """<p>7.2. <strong>Browser-Level Blocking and Deletion:</strong> Beyond our CMP, you can manage cookies comprehensively at the browser level. If you wish to delete all cookies currently stored on your device, or configure your browser to block third-party cookies globally, please follow the specific instructions provided by your browser manufacturer:</p>
        <div style="background-color: #f9f8f5; border-left: 4px solid var(--gold); padding: 1rem; margin-bottom: 1rem; font-size: 0.9rem;">
            <strong>Important Note on Local Storage:</strong> Simply clearing "cookies" in some older browsers may not automatically clear HTML5 Local Storage or Session Storage. To ensure all tracking technologies are removed, please ensure you select the option to clear "Cookies and other site data" or "Cached images and files" when clearing your browsing history.
        </div>"""
    content = content.replace(target_7_2, replacement_7_2)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print("Updated cookies.html with extra legal robustness.")

if __name__ == '__main__':
    update_cookies_file()
