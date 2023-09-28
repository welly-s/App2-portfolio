import streamlit as st

st.set_page_config(layout='wide')

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")  #use width to change image size

with col2:
    st.title("Ardic Sulce")
    content = """ Hello.. I am xxx
    nice to meet u.Type all the text here.
    bla bla blaaaaa"""
    #st.write(content)
    st.info(content)