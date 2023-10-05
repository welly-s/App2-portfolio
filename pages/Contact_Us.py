import streamlit as st
st.header("Contact Me")

with st.form(key='email_form'):
    user_email = st.text_input("Your email address", placeholder="Type your email here...")
    message = st.text_area("Your message")
    button = st.form_submit_button(label = 'submit')  #button is bollean
    if button:
        message = message + user_email
        