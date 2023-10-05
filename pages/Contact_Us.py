import streamlit as st
st.header("Contact Me")
from send_email import send_email

with (st.form(key='email_form')):
    user_email = st.text_input("Your email address", placeholder="Type your email here...")
    raw_message = st.text_area("Your message")
    message = f"""\
Subject: New email from {user_email}

From: {user_email}
{raw_message}
"""

    button = st.form_submit_button(label = 'submit')  #button is bollean
    if button:
        send_email(message)
        st.info("Your email was sent successfully")
