import streamlit as st
import pandas as pd
import requests

# Brevo API configuration
BREVO_API_KEY = 'your_brevo_api_key'
BREVO_API_URL = 'https://api.brevo.com/v3/smtp/email'

def send_email(recipient, subject, body):
    headers = {
        'accept': 'application/json',
        'api-key': BREVO_API_KEY,
        'content-type': 'application/json'
    }

    data = {
        "sender": {"name": "Your Name", "email": "your_email@example.com"},
        "to": [{"email": recipient}],
        "subject": subject,
        "htmlContent": body
    }

    response = requests.post(BREVO_API_URL, headers=headers, json=data)
    return response.status_code, response.json()

st.title('Email Sending Application')

uploaded_file = st.file_uploader("Choose a file with email IDs", type=["csv", "xlsx"])
subject = st.text_input("Subject")
body = st.text_area("Body")

if uploaded_file is not None and subject and body:
    try:
        if uploaded_file.name.endswith('.csv'):
            email_df = pd.read_csv(uploaded_file)
        else:
            email_df = pd.read_excel(uploaded_file)

        if 'email' not in email_df.columns:
            st.error("Uploaded file does not contain a column named 'email'.")
        else:
            email_list = email_df['email'].tolist()

            if st.button("Send Emails"):
                for email in email_list:
                    status_code, response = send_email(email, subject, body)
                    if status_code == 201:
                        st.success(f"Email sent to {email}")
                    else:
                        st.error(f"Failed to send email to {email}: {response}")
    except Exception as e:
        st.error(f"Error: {e}")
else:
    st.warning("Please upload a file and provide subject and body.")
