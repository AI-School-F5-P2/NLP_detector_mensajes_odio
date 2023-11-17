import streamlit as st 
from Scrapper.predict import predict_page
from Scrapper.Youtube import youtube_page
from Init.init import init, init_predict_comments, init_scrapping_css

# FUNCION PARA CREAR LOS ESTILOS Y TITULOS DE LA APP
init()

# SIDEBAR
page = st.sidebar.selectbox("Selecciona una página", ["Predict-Comments", "Scrapping"])

# PAGES
if page == "Predict-Comments":
    # CSS
    init_predict_comments(None)
    # label + input
    value_comment = st.text_area("", height=25, placeholder="Inserte un comentario...", key="comment_preddict", max_chars=1000)
    # button created
    button_preddict = st.button("Predict", key="predict_button",  type="primary", use_container_width=True)

    # if button is clicked
    if button_preddict:
        # predict
        try:
            predict_page(value_comment)
        except: 
            st.write("Inserte un comentario...")
elif page == "Scrapping":
    # CSS
    init_scrapping_css()
    # TEXT AREA
    value = st.text_area("", height=25, placeholder="Inserta un link de un video de youtube", key="youtube")

    # BUTTON centramos el button
    button = st.button("Scrappear", key="youtube_button", type="primary", use_container_width=True)
    # if button is clicked
    if button:
        # predict
        try:
            youtube_page(value)
        except:
            st.write("Inserta un link de un video de youtube")