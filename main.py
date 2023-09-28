import streamlit as st

st.set_page_config(layout='wide')

col1, col2 = st.columns(2)

with col1:
    st.image("images/photo.png")  #use width to change image size

with col2:
    st.title("Ardic Sulce")
    content = """ Hello I am Ardit! I am a python programmer, teacher and founder of PytonnHow. 
    I graduated in 2013 with a Master of Science in Geospatial Technologies from University of Muenster in German 
    with a focis on using Python for remote sensing. I have worked with companies from various countries,
     such as the Center for Conservation Geography, to map and understand Australian Ecosystems, image processing with 
     Swiss inTerra and performing data mining to gain business insights with the Australian Rapid Intelligence"""
    #st.write(content)
    st.info(content)

#st.text('Below you can find some of the apps that i have built in pythin. feel free to contact me'  )
st.write('Below you can find some of the apps that i have built in pythin. feel free to contact me'    )
#st.markdown('Below you can find some of the apps that i have built in pythin. feel free to contact me')