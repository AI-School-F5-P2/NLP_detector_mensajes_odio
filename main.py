
import json
import pandas as pd
import streamlit as st
import streamlit.components.v1 as components
from predict import predict_page
# secciones
page = st.sidebar.selectbox("Selecciona una página", ["Comentario", "Grupo de comentarios"])

# si la sección es "Visualización de Datos"
if page == "Comentario":
    # CSS
    st.markdown(
    """
    <style>
    .st-bo {
        overflow-y: hidden;
        display: flex !important;
        justify-content: space-around !important;
        margin-top: 20px !important;
    }
    .scale-in-center{-webkit-animation:scale-in-center .5s cubic-bezier(.25,.46,.45,.94) both;animation:scale-in-center .5s cubic-bezier(.25,.46,.45,.94) both}
    @-webkit-keyframes scale-in-center{0%{-webkit-transform:scale(0);transform:scale(0);opacity:1}100%{-webkit-transform:scale(1);transform:scale(1);opacity:1}}@keyframes scale-in-center{0%{-webkit-transform:scale(0);transform:scale(0);opacity:1}100%{-webkit-transform:scale(1);transform:scale(1);opacity:1}}

    </style>
    """,
        unsafe_allow_html=True
    )

    # Título de la app
    st.write("""
    <div class="scale-in-center" style="display: flex; justify-content: center; align-items: center; margin: 0px 0px 30px 0px;">
        <h1 style="font-size: 45px; text-align: center; border-bottom: 1px solid white;">Predecir comentarios toxicos</h1>
    </div>""", unsafe_allow_html=True)

    # IMAGE
    st.write("""
    <div style="display: flex; justify-content: center; align-items: center; box-shadow: rgba(0, 0, 0, 0.25) 0px 14px 28px, rgba(0, 0, 0, 0.22) 0px 10px 10px; padding: 10px;">
        <img src="https://media3.giphy.com/media/aKFw4ifPBEuxq/giphy.gif?cid=ecf05e47re5nkujjpiy3q4gxtk0albw09ybdql92b67012vg&ep=v1_gifs_search&rid=giphy.gif&ct=g" alt="aereolina" width="700" style="margin: 10px 0px; border-radius: 6px;">
    </div>""", unsafe_allow_html=True)

    # textarea 
    value_contents = st.text_area("", value="", height=None, max_chars=None, key=None, help=None, on_change=None, args=None, placeholder="Inserta un comentario...", disabled=False, label_visibility="visible")





    # si la sección es "Predicción"
    if st.button("Nivel de satisfacción"):
        predict_page(value_contents)
  
    # si la sección es "Visualización de Datos"
elif  page == "Grupo de comentarios":  
    st.write("""
    <div class="scale-in-center" style="display: flex; justify-content: center; align-items: center; margin: 0px 0px 30px 0px;">
        <h1 style="font-size: 45px; text-align: center; border-bottom: 1px solid white;">hola bomdia</h1>
    </div>""", unsafe_allow_html=True)


