import streamlit as st
from fraud_detector import is_fraudulent

st.set_page_config(page_title="UPI Fraud Blocker", layout="centered")

st.title("🔐 Real-Time UPI Fraud Blocker")

st.write("Check if a transaction is safe or potentially fraudulent.")

with st.form("fraud_check_form"):
    upi_id = st.text_input("Enter UPI ID")
    phone = st.text_input("Enter Phone Number")
    url = st.text_input("Paste Website/Link (if any)")
    apps = st.text_input("Running Apps (comma-separated e.g., WhatsApp, AnyDesk)")

    submitted = st.form_submit_button("Check Now")

    if submitted:
        app_list = [app.strip() for app in apps.split(",")]
        results = is_fraudulent(upi_id=upi_id, phone=phone, url=url, apps=app_list)

        if results:
            st.error("🚨 FRAUD DETECTED:")
            for reason in results:
                st.write(f"- {reason}")
        else:
            st.success("✅ No fraud detected. Proceed with caution.")
