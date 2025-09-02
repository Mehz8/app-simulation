import json

# Load fraud database
def load_blacklist():
    with open("database.json", "r") as f:
        return json.load(f)

def is_fraudulent(upi_id=None, phone=None, url=None, apps=[]):
    db = load_blacklist()
    reasons = []

    # Check UPI ID
    if upi_id and upi_id.lower() in db["upi_ids"]:
        reasons.append("UPI ID is blacklisted.")

    # Check Phone
    if phone and phone in db["phone_numbers"]:
        reasons.append("Phone number is blacklisted.")

    # Check URL
    if url:
        for keyword in db["phishing_keywords"]:
            if keyword in url.lower():
                reasons.append(f"URL contains phishing keyword: {keyword}")

    # Check for remote access apps
    for app in apps:
        if app.lower() in db["blocked_apps"]:
            reasons.append(f"Detected remote control app: {app}")

    return reasons