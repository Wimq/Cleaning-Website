import sys

def update_form():
    file_path = 'pages/legal/enquiry.html'
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Update Hero Title and Text
    old_hero = """        <div class="hero-content">
            <h1>Right to Erasure.</h1>
            <p>Under the UK General Data Protection Regulation (UK GDPR), you have the "Right to be Forgotten". Use this secure portal to formally request the permanent deletion of the personal data we hold about you.</p>
            
            <div class="contact-methods">
                <div class="method">
                    <i data-lucide="trash-2"></i>
                    <span>Permanent Data Deletion</span>
                </div>
                <div class="method">
                    <i data-lucide="clock"></i>
                    <span>Processed within 30 statutory days</span>
                </div>"""
                
    new_hero = """        <div class="hero-content">
            <h1>Data Rights Request.</h1>
            <p>Under the UK General Data Protection Regulation (UK GDPR), you are in control of your personal data. Use this secure portal to request a copy, update, or permanent deletion of your data.</p>
            
            <div class="contact-methods">
                <div class="method">
                    <i data-lucide="shield-check"></i>
                    <span>Manage Your Data Rights</span>
                </div>
                <div class="method">
                    <i data-lucide="clock"></i>
                    <span>Processed within 30 statutory days</span>
                </div>"""
    content = content.replace(old_hero, new_hero)

    # 2. Add Select Field to Form
    old_form_part = """                <div class="form-group">
                    <textarea id="enquiryBody" class="form-control" placeholder=" " required minlength="5"></textarea>
                    <label class="floating-label">Specific Details / Reason for Erasure</label>
                    <div class="error-message">Please provide a brief detail.</div>
                </div>

                <button type="submit" id="submitBtn" class="submit-btn" disabled>
                    Request Data Deletion <i data-lucide="shield-alert" style="width:18px;"></i>
                </button>"""
                
    new_form_part = """                <div class="form-group" style="margin-bottom: 3.5rem;">
                    <label style="position: absolute; top: -20px; left: 0; font-size: 0.8rem; color: var(--navy); font-weight: 600;">Type of Request</label>
                    <select id="requestType" class="form-control" required style="cursor: pointer;">
                        <option value="" disabled selected>Select an option...</option>
                        <option value="delete">Delete my data</option>
                        <option value="copy">Request a copy of my data (DSAR)</option>
                        <option value="update">Update my data</option>
                        <option value="other">Other</option>
                    </select>
                    <div class="error-message" style="bottom: -25px;">Please select a request type.</div>
                </div>

                <div class="form-group">
                    <textarea id="enquiryBody" class="form-control" placeholder=" " required minlength="5"></textarea>
                    <label class="floating-label">Specific Details</label>
                    <div class="error-message">Please provide brief details about your request.</div>
                </div>

                <button type="submit" id="submitBtn" class="submit-btn" disabled>
                    Submit Request <i data-lucide="shield-check" style="width:18px;"></i>
                </button>"""
    content = content.replace(old_form_part, new_form_part)
    
    # 3. Update Success message
    old_success = """            <h2>Request Submitted</h2>
            <p>Your formal request for data erasure has been securely transmitted to our compliance officer. We will process your request and confirm deletion within 30 days in accordance with UK GDPR.</p>"""
    new_success = """            <h2>Request Submitted</h2>
            <p>Your Data Rights request has been securely transmitted to our compliance officer. We will review your request and get back to you within 30 statutory days in accordance with UK GDPR.</p>"""
    content = content.replace(old_success, new_success)
    
    # 4. Update Title
    content = content.replace('<title>Right to Erasure | Kensington Ivy Ltd</title>', '<title>Data Rights Request | Kensington Ivy Ltd</title>')
    
    # 5. Fix JS validation for select
    js_old = """            if (!/^(\+?\d{10,15})$/.test(stripped)) {
                input.classList.add('invalid');
                return false;
            }
        }

        input.classList.remove('invalid');"""
        
    js_new = """            if (!/^(\+?\d{10,15})$/.test(stripped)) {
                input.classList.add('invalid');
                return false;
            }
        }
        
        if (input.tagName === 'SELECT' && input.value === '') {
            input.classList.add('invalid');
            return false;
        }

        input.classList.remove('invalid');"""
    content = content.replace(js_old, js_new)

    js_check_old = """    const inputs = form.querySelectorAll('input, textarea');"""
    js_check_new = """    const inputs = form.querySelectorAll('input, textarea, select');"""
    content = content.replace(js_check_old, js_check_new)

    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print("Success")

if __name__ == '__main__':
    update_form()
