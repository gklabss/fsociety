import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class SocialEngineeringEmail:
    def __init__(self):
        self.sent_emails = []

    def create_email_template(self, template_type="phishing"):
        """Create different email templates for educational purposes"""
        templates = {
            "phishing": {
                "subject": "Urgent: Account Security Update Required",
                "body": """
                Dear User,

                We have detected suspicious activity on your account. Please verify your account immediately by clicking on the link below:

                [VERIFY ACCOUNT NOW]

                If you do not verify within 24 hours, your account will be suspended.

                Best regards,
                Security Team
                """
            },
            "pretexting": {
                "subject": "Important Document for Your Review",
                "body": """
                Hello,

                Please find the attached document that requires your immediate attention. You will need to provide your credentials to access it.

                [ACCESS DOCUMENT]

                Thank you,
                Administration
                """
            }
        }
        return templates.get(template_type, templates["phishing"])

    def analyze_email_content(self, email_content):
        """Analyze email content for social engineering indicators"""
        indicators = []

        # Common social engineering indicators
        urgent_words = ["urgent", "immediate", "asap", "now", "24 hours"]
        action_words = ["click", "verify", "access", "login", "download"]
        fear_words = ["suspended", "locked", "compromised", "threat"]

        content_lower = email_content.lower()

        for word in urgent_words:
            if word in content_lower:
                indicators.append(f"Urgency indicator: '{word}'")

        for word in action_words:
            if word in content_lower:
                indicators.append(f"Action request: '{word}'")

        for word in fear_words:
            if word in content_lower:
                indicators.append(f"Fear tactic: '{word}'")

        return {
            "indicators": indicators,
            "risk_level": "High" if len(indicators) > 3 else "Medium" if len(indicators) > 1 else "Low"
        }

    def send_test_email(self, to_email, subject, body, from_email="test@example.com"):
        """Send a test email (for educational purposes only)"""
        # This is a mock implementation for educational purposes
        # In a real implementation, you would use actual SMTP
        email_data = {
            "to": to_email,
            "from": from_email,
            "subject": subject,
            "body": body,
            "timestamp": "2026-05-10"
        }

        self.sent_emails.append(email_data)
        return {
            "status": "sent",
            "message": f"Test email sent to {to_email} (simulation only)"
        }

def create_social_engineering_tool():
    """Factory function to create social engineering tool instance"""
    return SocialEngineeringEmail()