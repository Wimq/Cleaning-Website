import re
import sys

def main():
    file_path = "pages/legal/cookies.html"
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # 1. Replace Nav
    nav_pattern = r'<nav class="legal-nav-list">\s*<a href="#s1">1\. What Are Cookies\?</a>.*?</nav>'
    nav_replacement = """<nav class="legal-nav-list">
            <a href="#s1">1. What Are Cookies?</a>
            <a href="#s2">2. Our Legal Basis</a>
            <a href="#s3">3. Categories of Cookies</a>
            <a href="#s4">4. Full Cookie Inventory</a>
            <a href="#s5">5. Third-Party Relationships</a>
            <a href="#s6">6. Lifespans and Expiry</a>
            <a href="#s7">7. Your Choices &amp; Control</a>
            <a href="#s8">8. Policy Updates</a>
            <a href="#s9">9. Contact &amp; Complaints</a>
        </nav>"""
    
    # We only want to replace the second nav (the one under <h3>Contents</h3>)
    # The first nav is for Legal Hub, so we must be specific
    
    content = content.replace('''<nav class="legal-nav-list">
            <a href="#s1">1. What Are Cookies?</a>
            <a href="#s2">2. Our Legal Basis</a>
            <a href="#s3">3. Cookies We Use</a>
            <a href="#s4">4. Third-Party Cookies</a>
            <a href="#s5">5. How Long Cookies Last</a>
            <a href="#s6">6. Your Choices</a>
            <a href="#s7">7. Changes to Policy</a>
            <a href="#s8">8. Contact</a>
        </nav>''', nav_replacement)

    # 2. Replace Document Content
    new_doc_content = """<h2 id="s1">1. What Are Cookies and Similar Technologies?</h2>
        <p>1.1. This Cookie Policy explains how <strong>KENSINGTON IVY LTD</strong> (Companies House No. 17167406, registered at 453 South End Road, Hornchurch, England, RM12 5NX) ("we", "us", "our") uses cookies and similar tracking technologies on our website at <strong>kensingtonivy.co.uk</strong> (the "Website"). It should be read alongside our <a href="privacy.html" style="color:var(--gold);font-weight:600;">Privacy Policy</a>.</p>
        <p>1.2. <strong>Cookies:</strong> Cookies are small text files placed on your device (computer, smartphone, or tablet) by a web server when you visit a website. They allow the website to recognise your device across sessions and can store preferences, session information, and usage data. Cookies cannot execute programmes or carry viruses; they are simply files that enable websites to function more efficiently and provide information to the website owner.</p>
        <p>1.3. <strong>Similar Technologies:</strong> In addition to cookies, we may use related tracking technologies, which are collectively referred to as "cookies" throughout this policy for simplicity. These include:</p>
        <ul>
            <li><strong>Web Beacons / Pixels:</strong> Small transparent image files or lines of code embedded in web pages or emails. They record that a user has visited a specific web page or opened an email, helping us measure the effectiveness of our campaigns (e.g., Meta Pixel).</li>
            <li><strong>Local Storage &amp; Session Storage:</strong> Web storage technologies that allow data to be stored locally within your browser rather than sent to the server with every HTTP request. This is often used for saving user interface preferences or temporary session data.</li>
        </ul>
        <p>1.4. <strong>First-Party vs. Third-Party:</strong> <em>First-party cookies</em> are set directly by kensingtonivy.co.uk. <em>Third-party cookies</em> are set by a domain other than the one you are currently visiting (such as Google or LinkedIn) to provide analytics or advertising services.</p>

        <h2 id="s2">2. Our Legal Basis and Consent Standard</h2>
        <p>2.1. Our use of cookies is governed by the <strong>Privacy and Electronic Communications Regulations 2003 (PECR)</strong>, as amended, read alongside the <strong>UK General Data Protection Regulation (UK GDPR)</strong> and the <strong>Data Protection Act 2018 (DPA 2018)</strong>.</p>
        <p>2.2. Under Regulation 6 of PECR:</p>
        <ul>
            <li><strong>Strictly Necessary Cookies</strong> may be placed without your consent, as they are essential for the Website to function and cannot be switched off. We rely on our legitimate interests (Article 6(1)(f) UK GDPR) to process any personal data gathered by these cookies.</li>
            <li><strong>All other cookies</strong> (Analytics, Functional, and Marketing) require your <strong>prior, freely given, specific, informed, and unambiguous consent</strong> (Article 6(1)(a) UK GDPR) before they are set.</li>
        </ul>
        <p>2.3. <strong>Our Consent Mechanism:</strong> We obtain this consent via our Cookie Consent Management Platform (CMP), which is displayed to all first-time visitors to the Website. We strictly adhere to the following principles:</p>
        <ul>
            <li><strong>No Pre-Ticked Boxes:</strong> All non-essential cookie categories are disabled by default.</li>
            <li><strong>Granular Choice:</strong> You can consent to specific categories of cookies independently.</li>
            <li><strong>No Cookie Walls:</strong> Access to our Website is not contingent on you accepting non-essential cookies.</li>
            <li><strong>Easy Withdrawal:</strong> Withdrawing consent is as easy as giving it. You can manage your preferences at any time via the "Cookie Settings" link in the footer.</li>
        </ul>
        <p>2.4. We maintain a secure, pseudonymised audit log of all consent obtained, including the timestamp, the consent version presented, and the specific categories consented to, to demonstrate compliance under the accountability principle (Article 5(2) UK GDPR).</p>

        <h2 id="s3">3. Categories of Cookies We Use</h2>
        <p>3.1. We categorise the cookies used on our Website strictly into four groups based on their function and purpose.</p>

        <h3>Category 1: Strictly Necessary Cookies (Always Active)</h3>
        <p>These cookies are strictly required to operate our Website securely and efficiently. They enable core functions such as page navigation, accessing secure areas, load balancing, preventing cross-site request forgery (CSRF), and remembering your cookie consent preferences. Because the Website cannot function properly without these cookies, <strong>consent is not required under PECR</strong>. However, you can configure your browser to block these cookies, though this will result in parts of the Website breaking or becoming inaccessible.</p>

        <h3>Category 2: Analytics &amp; Performance Cookies (Requires Consent)</h3>
        <p>These cookies collect aggregated, anonymised information about how visitors use our Website. They help us understand which pages are the most and least popular, how visitors navigate the site, and if they encounter any error messages. This information is used exclusively to improve the performance and design of our Website. <strong>These cookies are only set if you explicitly opt-in.</strong></p>

        <h3>Category 3: Functional Cookies (Requires Consent)</h3>
        <p>These cookies allow our Website to remember choices you make (such as your language preference, region, or customized interface elements like text size or dark mode) and provide enhanced, highly personalised features. They may be set by us or by third-party providers whose services we have added to our pages. <strong>These cookies are only set if you explicitly opt-in.</strong></p>

        <h3>Category 4: Marketing &amp; Targeting Cookies (Requires Consent)</h3>
        <p>These cookies are set by our selected advertising partners (e.g., Google, LinkedIn, Meta). They are used to build a profile of your interests based on your browsing activity and deliver relevant advertisements to you on other websites and social media platforms. They do not store direct personal information but uniquely identify your browser and internet device. <strong>These cookies are only set if you explicitly opt-in.</strong></p>

        <h2 id="s4">4. Full Cookie Inventory and Audit</h2>
        <p>4.1. The following table lists every cookie currently in use on this Website. We conduct regular audits (at least quarterly) to ensure this inventory remains completely accurate.</p>

        <div style="overflow-x:auto;margin:1.5rem 0;">
        <table style="width:100%;border-collapse:collapse;font-size:0.85rem;">
            <thead>
                <tr style="background:var(--navy);color:#fff;">
                    <th style="padding:10px 14px;text-align:left;border:1px solid rgba(255,255,255,.15);">Cookie Name</th>
                    <th style="padding:10px 14px;text-align:left;border:1px solid rgba(255,255,255,.15);">Provider</th>
                    <th style="padding:10px 14px;text-align:left;border:1px solid rgba(255,255,255,.15);">Purpose</th>
                    <th style="padding:10px 14px;text-align:left;border:1px solid rgba(255,255,255,.15);">Category</th>
                    <th style="padding:10px 14px;text-align:left;border:1px solid rgba(255,255,255,.15);">Type</th>
                    <th style="padding:10px 14px;text-align:left;border:1px solid rgba(255,255,255,.15);">Duration</th>
                </tr>
            </thead>
            <tbody>
                <tr style="background:#f9f8f5;">
                    <td style="padding:9px 14px;border:1px solid #e0ddd5;">ki_cookie_consent</td>
                    <td style="padding:9px 14px;border:1px solid #e0ddd5;">Kensington Ivy</td>
                    <td style="padding:9px 14px;border:1px solid #e0ddd5;">Stores your cookie consent preference (categories accepted/rejected) to prevent re-showing the banner.</td>
                    <td style="padding:9px 14px;border:1px solid #e0ddd5;">Strictly Necessary</td>
                    <td style="padding:9px 14px;border:1px solid #e0ddd5;">First-Party</td>
                    <td style="padding:9px 14px;border:1px solid #e0ddd5;">12 months</td>
                </tr>
                <tr>
                    <td style="padding:9px 14px;border:1px solid #e0ddd5;">PHPSESSID / session</td>
                    <td style="padding:9px 14px;border:1px solid #e0ddd5;">Kensington Ivy</td>
                    <td style="padding:9px 14px;border:1px solid #e0ddd5;">Maintains an active browsing session and preserves multi-step form data.</td>
                    <td style="padding:9px 14px;border:1px solid #e0ddd5;">Strictly Necessary</td>
                    <td style="padding:9px 14px;border:1px solid #e0ddd5;">First-Party</td>
                    <td style="padding:9px 14px;border:1px solid #e0ddd5;">Session</td>
                </tr>
                <tr style="background:#f9f8f5;">
                    <td style="padding:9px 14px;border:1px solid #e0ddd5;">XSRF-TOKEN / csrf</td>
                    <td style="padding:9px 14px;border:1px solid #e0ddd5;">Kensington Ivy</td>
                    <td style="padding:9px 14px;border:1px solid #e0ddd5;">Security token protecting against cross-site request forgery (CSRF) attacks.</td>
                    <td style="padding:9px 14px;border:1px solid #e0ddd5;">Strictly Necessary</td>
                    <td style="padding:9px 14px;border:1px solid #e0ddd5;">First-Party</td>
                    <td style="padding:9px 14px;border:1px solid #e0ddd5;">Session</td>
                </tr>
                <tr>
                    <td style="padding:9px 14px;border:1px solid #e0ddd5;">_ga</td>
                    <td style="padding:9px 14px;border:1px solid #e0ddd5;">Google LLC</td>
                    <td style="padding:9px 14px;border:1px solid #e0ddd5;">Distinguishes unique visitors; generates statistical data on Website usage (GA4).</td>
                    <td style="padding:9px 14px;border:1px solid #e0ddd5;">Analytics</td>
                    <td style="padding:9px 14px;border:1px solid #e0ddd5;">Third-Party</td>
                    <td style="padding:9px 14px;border:1px solid #e0ddd5;">2 years</td>
                </tr>
                <tr style="background:#f9f8f5;">
                    <td style="padding:9px 14px;border:1px solid #e0ddd5;">_ga_*</td>
                    <td style="padding:9px 14px;border:1px solid #e0ddd5;">Google LLC</td>
                    <td style="padding:9px 14px;border:1px solid #e0ddd5;">Maintains GA4 session state, engagement metrics, and campaign data.</td>
                    <td style="padding:9px 14px;border:1px solid #e0ddd5;">Analytics</td>
                    <td style="padding:9px 14px;border:1px solid #e0ddd5;">Third-Party</td>
                    <td style="padding:9px 14px;border:1px solid #e0ddd5;">2 years</td>
                </tr>
                <tr>
                    <td style="padding:9px 14px;border:1px solid #e0ddd5;">_gid</td>
                    <td style="padding:9px 14px;border:1px solid #e0ddd5;">Google LLC</td>
                    <td style="padding:9px 14px;border:1px solid #e0ddd5;">Identifies unique visitors within a 24-hour period for daily usage stats.</td>
                    <td style="padding:9px 14px;border:1px solid #e0ddd5;">Analytics</td>
                    <td style="padding:9px 14px;border:1px solid #e0ddd5;">Third-Party</td>
                    <td style="padding:9px 14px;border:1px solid #e0ddd5;">24 hours</td>
                </tr>
                <tr style="background:#f9f8f5;">
                    <td style="padding:9px 14px;border:1px solid #e0ddd5;">ki_preferences</td>
                    <td style="padding:9px 14px;border:1px solid #e0ddd5;">Kensington Ivy</td>
                    <td style="padding:9px 14px;border:1px solid #e0ddd5;">Local storage key that remembers interface preferences (e.g., accessibility settings, region) across sessions.</td>
                    <td style="padding:9px 14px;border:1px solid #e0ddd5;">Functional</td>
                    <td style="padding:9px 14px;border:1px solid #e0ddd5;">First-Party</td>
                    <td style="padding:9px 14px;border:1px solid #e0ddd5;">12 months</td>
                </tr>
                <tr>
                    <td style="padding:9px 14px;border:1px solid #e0ddd5;">li_sugr / AnalyticsSyncHistory / UserMatchHistory</td>
                    <td style="padding:9px 14px;border:1px solid #e0ddd5;">LinkedIn Ireland</td>
                    <td style="padding:9px 14px;border:1px solid #e0ddd5;">LinkedIn Insight Tag — measures campaign effectiveness; builds retargeting audiences for B2B recruitment ads.</td>
                    <td style="padding:9px 14px;border:1px solid #e0ddd5;">Marketing</td>
                    <td style="padding:9px 14px;border:1px solid #e0ddd5;">Third-Party</td>
                    <td style="padding:9px 14px;border:1px solid #e0ddd5;">90 days - 1 year</td>
                </tr>
                <tr style="background:#f9f8f5;">
                    <td style="padding:9px 14px;border:1px solid #e0ddd5;">_gcl_au / AW-*</td>
                    <td style="padding:9px 14px;border:1px solid #e0ddd5;">Google LLC</td>
                    <td style="padding:9px 14px;border:1px solid #e0ddd5;">Google Ads Conversion Tracking — measures form submissions originating from Google ad clicks.</td>
                    <td style="padding:9px 14px;border:1px solid #e0ddd5;">Marketing</td>
                    <td style="padding:9px 14px;border:1px solid #e0ddd5;">Third-Party</td>
                    <td style="padding:9px 14px;border:1px solid #e0ddd5;">90 days</td>
                </tr>
                <tr>
                    <td style="padding:9px 14px;border:1px solid #e0ddd5;">_fbp / fr</td>
                    <td style="padding:9px 14px;border:1px solid #e0ddd5;">Meta Platforms Ireland</td>
                    <td style="padding:9px 14px;border:1px solid #e0ddd5;">Meta Pixel — tracks conversions from Facebook/Instagram ads; enables dynamic retargeting audiences.</td>
                    <td style="padding:9px 14px;border:1px solid #e0ddd5;">Marketing</td>
                    <td style="padding:9px 14px;border:1px solid #e0ddd5;">Third-Party</td>
                    <td style="padding:9px 14px;border:1px solid #e0ddd5;">180 days</td>
                </tr>
            </tbody>
        </table>
        </div>

        <h2 id="s5">5. Third-Party Relationships and Joint Controllership</h2>
        <p>5.1. <strong>Third-Party Processors:</strong> Some cookies on our Website are placed by third-party service providers (as detailed in Section 4). While we control the decision to implement these tools, the third parties govern the specific cookie mechanics. We have executed comprehensive Data Processing Agreements (DPAs), incorporating UK Standard Contractual Clauses (SCCs) where necessary, with all third-party providers to safeguard your data.</p>
        <p>5.2. <strong>Joint Controllership (Meta):</strong> In the case of the Meta Pixel, Kensington Ivy Ltd and Meta Platforms Ireland Limited act as "Joint Controllers" under Article 26 of the UK GDPR specifically for the collection and transmission of your data to Meta. Meta is an independent data controller for any subsequent processing. You can read Meta's privacy policy at <a href="https://www.facebook.com/privacy/policy" target="_blank" rel="noopener noreferrer" style="color:var(--gold);">facebook.com/privacy/policy</a>.</p>
        <p>5.3. <strong>Other Third-Party Policies:</strong> We encourage you to review the privacy policies of our other key partners:</p>
        <ul>
            <li><strong>Google (Analytics &amp; Ads):</strong> <a href="https://policies.google.com/privacy" target="_blank" rel="noopener noreferrer" style="color:var(--gold);">policies.google.com/privacy</a></li>
            <li><strong>LinkedIn:</strong> <a href="https://www.linkedin.com/legal/privacy-policy" target="_blank" rel="noopener noreferrer" style="color:var(--gold);">linkedin.com/legal/privacy-policy</a></li>
        </ul>

        <h2 id="s6">6. Cookie Lifespans and Expiry</h2>
        <p>6.1. Cookies have varying lifespans designed to fulfill their specific purpose:</p>
        <ul>
            <li><strong>Session Cookies:</strong> These are temporary strings of code deleted automatically by your device operating system the moment you close your browser tab or window. They are used for immediate state-preservation, such as keeping you logged into an account portal.</li>
            <li><strong>Persistent Cookies:</strong> These remain on your device's hard drive after your browser is closed, continuing to exist until their predefined expiration date is reached or you manually delete them. We mandate that no persistent tracking cookie exceeds a lifespan of 24 months. Furthermore, we configure our consent cookie (ki_cookie_consent) to expire after 12 months, meaning we will ask for your consent again annually.</li>
        </ul>

        <h2 id="s7">7. Your Comprehensive Rights and Cookie Control</h2>
        <p>7.1. <strong>Instant Preference Management via Our CMP:</strong> You maintain absolute control over the non-essential cookies on this Website. You can revoke or amend your consent at any time, instantly, by clicking the <strong>"Cookie Settings"</strong> button located in the footer of every page. Withdrawing consent does not affect the lawfulness of processing based on consent before its withdrawal.</p>
        <p>7.2. <strong>Browser-Level Blocking and Deletion:</strong> Beyond our CMP, you can manage cookies comprehensively at the browser level. If you wish to delete all cookies currently stored on your device, or configure your browser to block third-party cookies globally, please follow the specific instructions provided by your browser manufacturer:</p>
        <ul>
            <li><strong>Google Chrome:</strong> Go to Settings &gt; Privacy and security &gt; Cookies and other site data. <a href="https://support.google.com/chrome/answer/95647" target="_blank" rel="noopener noreferrer" style="color:var(--gold);">Read Chrome Guide</a>.</li>
            <li><strong>Safari (macOS):</strong> Go to Safari &gt; Preferences &gt; Privacy. <a href="https://support.apple.com/en-gb/guide/safari/sfri11471/mac" target="_blank" rel="noopener noreferrer" style="color:var(--gold);">Read Safari Guide</a>.</li>
            <li><strong>Safari (iOS/iPadOS):</strong> Go to Settings &gt; Safari &gt; Advanced &gt; Website Data.</li>
            <li><strong>Mozilla Firefox:</strong> Go to Preferences &gt; Privacy &amp; Security &gt; Cookies and Site Data. <a href="https://support.mozilla.org/en-US/kb/clear-cookies-and-site-data-firefox" target="_blank" rel="noopener noreferrer" style="color:var(--gold);">Read Firefox Guide</a>.</li>
            <li><strong>Microsoft Edge:</strong> Go to Settings &gt; Cookies and site permissions &gt; Manage and delete cookies and site data.</li>
            <li><strong>Android (Chrome):</strong> Go to Chrome menu &gt; Settings &gt; Site settings &gt; Cookies.</li>
        </ul>
        <p>7.3. <strong>Industry-Wide Opt-Out Tools:</strong> If you wish to opt-out of targeted advertising broadly across the internet (not just on our Website), you can utilise independent, industry-regulated tools:</p>
        <ul>
            <li><strong>European Interactive Digital Advertising Alliance (EDAA):</strong> <a href="https://www.youronlinechoices.com/uk/" target="_blank" rel="noopener noreferrer" style="color:var(--gold);">youronlinechoices.com/uk/</a></li>
            <li><strong>Network Advertising Initiative (NAI):</strong> <a href="https://optout.networkadvertising.org/" target="_blank" rel="noopener noreferrer" style="color:var(--gold);">optout.networkadvertising.org</a></li>
            <li><strong>Google Analytics Specific Opt-Out:</strong> <a href="https://tools.google.com/dlpage/gaoptout" target="_blank" rel="noopener noreferrer" style="color:var(--gold);">tools.google.com/dlpage/gaoptout</a></li>
        </ul>
        <p>7.4. <strong>Global Privacy Control (GPC) / Do Not Track (DNT):</strong> We respect the Global Privacy Control (GPC) signal. If your browser transmits a valid GPC signal, our CMP will automatically interpret this as a rejection of all non-essential cookies. We monitor ongoing developments regarding the older Do Not Track (DNT) header, but currently, GPC is the supported standard for automated preference signalling.</p>

        <h2 id="s8">8. Policy Updates</h2>
        <p>8.1. We pledge to review this Cookie Policy at least annually, or whenever significant changes are made to the cookies we deploy or relevant legal frameworks (e.g., updates from the ICO or the anticipated UK Data Protection and Digital Information Bill). The "Effective Date" at the top of the policy will consistently reflect the latest version.</p>
        <p>8.2. Should material changes occur—such as the introduction of a new marketing provider or a change in processing purpose—we will force the Cookie Consent banner to reappear for all users to ensure re-consent is obtained transparently.</p>

        <h2 id="s9">9. Contact and Complaints</h2>
        <p>9.1. For any questions, data subject access requests, or concerns regarding our cookie practices, please contact our Data Protection and Compliance Team:</p>
        <ul>
            <li><strong>Email:</strong> compliance@kensingtonivy.co.uk</li>
            <li><strong>Post:</strong> Data Compliance, Kensington Ivy Ltd, 453 South End Road, Hornchurch, England, RM12 5NX (Companies House No. 17167406)</li>
        </ul>
        <p>9.2. <strong>Regulatory Recourse:</strong> You have the absolute right to lodge a formal complaint with the UK's supervisory authority for data protection, the <strong>Information Commissioner's Office (ICO)</strong>, if you believe we are processing your data unlawfully or violating PECR guidelines.</p>
        <ul>
            <li><strong>ICO Website:</strong> <a href="https://ico.org.uk/make-a-complaint/" target="_blank" rel="noopener noreferrer" style="color:var(--gold);">ico.org.uk/make-a-complaint</a></li>
            <li><strong>ICO Telephone:</strong> 0303 123 1113</li>
            <li><strong>Our ICO Registration Number:</strong> ZC148985</li>
        </ul>"""

    # We need to replace from <h2 id="s1">1. What Are Cookies?</h2> down to the end of the </main> container
    # Let's find the start and end indices
    start_str = '<h2 id="s1">1. What Are Cookies?</h2>'
    end_str = '</main>'
    
    start_idx = content.find(start_str)
    end_idx = content.find(end_str)
    
    if start_idx != -1 and end_idx != -1:
        # Include the print button at the top of the main document?
        # The print button is BEFORE <h2 id="s1">.
        # Wait, let's look at the structure:
        # <main class="legal-document">
        #     <div class="legal-actions">
        #         <button class="btn-print" onclick="window.print()"><i data-lucide="printer"></i> Print</button>
        #     </div>
        #     <h2 id="s1">1. What Are Cookies?</h2>
        # So replacing from <h2 id="s1"> down to </main> is perfect.
        content = content[:start_idx] + new_doc_content + '\n    ' + end_str + content[end_idx + len(end_str):]
        
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        print("Success: Cookie policy updated.")
    else:
        print("Error: Could not find start or end strings.")

if __name__ == "__main__":
    main()
