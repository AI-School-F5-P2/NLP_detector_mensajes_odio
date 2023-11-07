import time
import json
import pandas as pd
import streamlit as st# secciones
page = st.sidebar.selectbox("Selecciona una página", ["Comentarios", "comentariosss"])

# si la sección es "Visualización de Datos"
if page == "Comentarios":
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
    <div style="display: flex; justify-content: center; align-items: center; margin: 0px 0px 30px 0px;">
        <h1 style="font-size: 45px; text-align: center; border-bottom: 1px solid white;">Predict text</h1>
    </div>""", unsafe_allow_html=True)

    # IMAGE
    # st.write("""
    # <div style="display: flex; justify-content: center; align-items: center; box-shadow: rgba(0, 0, 0, 0.25) 0px 14px 28px, rgba(0, 0, 0, 0.22) 0px 10px 10px; padding: 10px;">
    #     <img src="https://i.pinimg.com/originals/b9/b8/1a/b9b81ab0e549a0ef6bbd9616e32031d5.gif" alt="aereolina" width="700" style="margin: 10px 0px; border-radius: 6px;">
    # </div>""", unsafe_allow_html=True)

    # # FIRST TEXT
    # st.write("""
    # <div style="margin: 10px 0px; display: flex; justify-content: center; align-items: center; box-shadow: rgba(0, 0, 0, 0.25) 0px 14px 28px, rgba(0, 0, 0, 0.22) 0px 10px 10px; padding: 10px;">
    #     <p style="font-size: 16px;">F5 Airlines lleva un tiempo recogiendo datos relativos a la satisfacción de los clientes. Esos datos han sido utilizados en general, pero con poco éxito, para ser analizados a mano en busca de los motivos y de un plan de actuación futuro para evitar este tipo de casos.</p>
    # </div>""", unsafe_allow_html=True)




    # button created
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["Youtube", "Facebook", "Twitter", "Instagram", "TikTok"])

    with tab1:
        try:
            exec(open("./Scrapper/Youtube.py").read())
        except Exception as e:
            st.error(f"Error al cargar los gráficos: {e}")
    with tab2:
        try:    
            exec(open("./Scrapper/Facebook.py").read())
        except Exception as e:
            st.error(f"Error al cargar los gráficos: {e}")
    with tab3:
        try:
            st.write("seccion de datos")
            exec(open("./Scrapper/Twitter.py").read())
        except Exception as e:
            st.error(f"Error al cargar los gráficos: {e}")
    with tab4:
        try:
            st.write("seccion de datosasdasd")
            # exec(open("./ML.py").read())
        except Exception as e:
            st.error(f"Error al cargar los gráficos: {e}")
    with tab5:
        try:
            st.write("seccion de datosasdasd")
            # exec(open("./ML.py").read())
        except Exception as e:
            st.error(f"Error al cargar los gráficos: {e}")

else:  
    st.write("hola como estamos todos")