import os
import glob
import re

new_banner = """
<!-- Detailed Cookie Banner -->
<div class="cookie-banner" id="cookieBanner">
    <div class="cookie-banner-inner">
        <div class="cookie-banner-text">
            <strong>Cookies on the Kensington Ivy website</strong>
            <p>We use some essential cookies to make this site work.</p>
            <p>We'd like to set analytics cookies to understand how you use this site. We may use services from YouTube that may also use cookies.</p>
            <p>For more detailed information, see our <a href="/pages/legal/cookies.html">Cookies page</a>.</p>
        </div>
        <div class="cookie-banner-actions">
            <button class="cookie-btn-accept" id="cookieAcceptAll">Accept all cookies</button>
            <button class="cookie-btn-necessary" id="cookieNecessary">Reject non-essential cookies</button>
            <button class="cookie-btn-settings" id="cookieSettingsBtn" onclick="document.getElementById('cookieDetails').classList.toggle('expanded');">Manage preferences</button>
        </div>

        <div class="cookie-banner-details" id="cookieDetails">
            <div class="cookie-section">
                <div class="cookie-section-header">
                    <h4>Essential cookies</h4>
                    <label class="cookie-toggle">
                        <input type="checkbox" checked disabled>
                        <span class="cookie-slider"></span>
                    </label>
                </div>
                <p>These cookies are necessary for core functionality, such as security and network management. They always need to be on.</p>
            </div>
            
            <div class="cookie-section">
                <div class="cookie-section-header">
                    <h4>Analytics cookies</h4>
                    <label class="cookie-toggle">
                        <input type="checkbox" id="toggleAnalytics">
                        <span class="cookie-slider"></span>
                    </label>
                </div>
                <p>We use analytics cookies to measure how you use our website to help us improve the experience.</p>
            </div>

            <div class="cookie-section">
                <div class="cookie-section-header">
                    <h4>Video player cookies</h4>
                    <label class="cookie-toggle">
                        <input type="checkbox" id="toggleVideo">
                        <span class="cookie-slider"></span>
                    </label>
                </div>
                <p>Pages that include videos hosted on YouTube may result in video platforms collecting information.</p>
            </div>

            <button class="cookie-btn-save" id="cookieSaveBtn">Save and close</button>
        </div>
    </div>
</div>
<script>
(function(){
    if(!localStorage.getItem("ki_cookie_consent")){
        setTimeout(function(){document.getElementById("cookieBanner").classList.add("visible");},800);
    }
    function logConsent(consentData){
        localStorage.setItem("ki_cookie_consent", typeof consentData === 'string' ? consentData : "custom");
        document.getElementById("cookieBanner").classList.remove("visible");
        fetch("/api/log-consent", {
            method: "POST",
            headers: {"Content-Type": "application/json"},
            body: JSON.stringify({consent: consentData})
        }).catch(function(){});
    }

    document.getElementById("cookieAcceptAll").addEventListener("click",function(){
        document.getElementById("toggleAnalytics").checked = true;
        document.getElementById("toggleVideo").checked = true;
        logConsent("all");
    });
    
    document.getElementById("cookieNecessary").addEventListener("click",function(){
        document.getElementById("toggleAnalytics").checked = false;
        document.getElementById("toggleVideo").checked = false;
        logConsent("necessary");
    });
    
    document.getElementById("cookieSaveBtn").addEventListener("click", function(){
        const analytics = document.getElementById("toggleAnalytics").checked;
        const video = document.getElementById("toggleVideo").checked;
        if(analytics && video) {
            logConsent("all");
        } else if (!analytics && !video) {
            logConsent("necessary");
        } else {
            logConsent("custom_analytics:" + analytics + "_video:" + video);
        }
    });
})();
</script>
</body>"""

def update_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()
    
    if "<!-- Detailed Cookie Banner -->" in content:
        print(f"Banner already in {filepath}")
        return

    # If it has the old cookie banner, we already replaced it in the first script.
    # The files that failed earlier DO NOT have any cookie banner at all.
    # So we just inject it before </body>
    
    if '</body>' in content:
        new_content = content.replace('</body>', new_banner)
        with open(filepath, 'w') as f:
            f.write(new_content)
        print(f"Injected banner into {filepath}")
    else:
        print(f"Could not find </body> in {filepath}")

for file in glob.glob('pages/**/*.html', recursive=True):
    update_file(file)
