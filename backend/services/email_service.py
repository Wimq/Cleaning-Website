import os
import json
import urllib.request
import urllib.error

# Load .env manually to avoid python-dotenv requirement
ENV_FILE = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))), ".env")
env_vars = {}
if os.path.exists(ENV_FILE):
    with open(ENV_FILE, "r") as f:
        for line in f:
            if "=" in line:
                key, val = line.strip().split("=", 1)
                env_vars[key] = val

RESEND_API_KEY = env_vars.get("RESEND_API_KEY", "")

def send_confirmation_email(name: str, email: str, course: str):
    if not RESEND_API_KEY or not email:
        print("DEBUG: Bailing out of send_confirmation_email due to missing key or email")
        return False
    
    html_body = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <title>Kensington Ivy | Admissions</title>
    </head>
    <body style="margin: 0; padding: 0; background-color: #ffffff; font-family: -apple-system, BlinkMacSystemFont, 'Helvetica Neue', Helvetica, Arial, sans-serif;">
        <table border="0" cellpadding="0" cellspacing="0" width="100%" style="max-width: 600px; margin: 40px auto; background-color: #ffffff; border: 1px solid #e5e7eb;">
            <tr>
                <td style="padding: 40px; text-align: center; border-top: 4px solid #0a1128;">
                    <h1 style="margin: 0; color: #0a1128; font-family: 'Georgia', serif; font-size: 24px; font-weight: normal; text-transform: uppercase;">Kensington<span style="color: #c9a258;">Ivy</span></h1>
                </td>
            </tr>
            <tr>
                <td style="padding: 10px 40px 40px 40px; color: #111827; line-height: 1.8;">
                    <h2 style="margin: 0 0 25px 0; color: #0a1128; font-family: 'Georgia', serif; font-size: 22px;">Dear {name},</h2>
                    <p>Thank you for your application to Kensington Ivy. We have successfully received your details.</p>
                    <table border="0" cellpadding="0" cellspacing="0" width="100%" style="margin: 30px 0; background-color: #f9fafb; border: 1px solid #f3f4f6;">
                        <tr>
                            <td style="padding: 20px;">
                                <span style="color: #6b7280; font-size: 12px; font-weight: 600;">Requested Course</span><br>
                                <strong style="color: #111827; font-size: 16px;">{course or 'General Enquiry'}</strong>
                            </td>
                        </tr>
                    </table>
                    <p>One of our admissions consultants will be in touch with you within 24 hours.</p>
                </td>
            </tr>
        </table>
    </body>
    </html>
    """
    
    req = urllib.request.Request('https://api.resend.com/emails', method='POST')
    req.add_header('Authorization', f'Bearer {RESEND_API_KEY}')
    req.add_header('Content-Type', 'application/json')
    req.add_header('User-Agent', 'KensingtonIvy-API/1.0')
    
    email_data = {
        "from": "Kensington Ivy Admissions <onboarding@resend.dev>",
        "to": [email],
        "subject": "Application Received - Kensington Ivy",
        "html": html_body
    }
    
    try:
        urllib.request.urlopen(req, data=json.dumps(email_data).encode('utf-8'))
        print(f"Confirmation email sent to {email}")
        return True
    except Exception as e:
        print(f"Failed to send email: {e}")
        return False
