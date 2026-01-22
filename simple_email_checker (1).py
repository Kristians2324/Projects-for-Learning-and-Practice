print("📧 Incoming Email Check...\n")

# Email Data
sender = "security@yourb4nk-test.com"
subject = "URGENT: Action Required on Your Account"
link = "http://verify-identity-login.com"
message = "We noticed a login from a new device. Please click the link to update your password immediately."

is_suspicious = False
reasons = []

# 1. Expanded List of Suspicious Terms
# By using a list, you can add dozens of words without making the code messy
suspicious_terms = [
    "verify", "pay", "delete", "money", "credit card", "personal info", "social security number",
    "bank account", "password", "update", "identity", "social security", "account blocked", "million",
    "suspended", "login", "won", "prize", "gift card", "limited time", "immediately", "suspicious",
    "urgent", "bank details", "malware", "hacked", "lottery", "virus", "security alert", "WARNING!",

]

# Check message for terms
for word in suspicious_terms:
    if word in message.lower():
        is_suspicious = True
        reasons.append(f"Suspicious word found: {word}")
        break

# 2. Check for Urgency/Threats
urgency_terms = ["urgent", "immediately", "action required", "locked", "final notice"]
for word in urgency_terms:
    if word in subject.lower():
        is_suspicious = True
        reasons.append("Subject line uses high-pressure urgency.")
        break

# 3. Check for Insecure Links (HTTP vs HTTPS)
if link.startswith("http://"):
    is_suspicious = True
    reasons.append("Link is insecure (http).")

# Final Result
if is_suspicious:
    print("⚠️  Warning: This email looks suspicious! Be careful.")
    print("Reasons found:")
    for reason in reasons:
        print(f" - {reason}")
else:
    print("✅ This email seems safe.")