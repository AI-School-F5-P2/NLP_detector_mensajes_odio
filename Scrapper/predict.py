import streamlit as st
from Components.CardComplement import CardComplement
from Scrapper.Predict_comments import predict_comments

def predict_page(value_contents):
    '''
    Función que se encarga de mostrar el resultado de la predicción
    atravez de un componente CardComplement que se encuentra en Components/CardComplement.py
    primero se muestra un spinner mientras se realiza la predicción, luego se muestra el resultado
    '''
    result = None
    if value_contents:
        # Muestra un spinner mientras se realiza la predicción
        with st.spinner("Prediciendo..."):
            result = predict_comments(value_contents)
            if result:
                CardComplement(value_contents, result[0]["score"], result[0]["label"])
            else:
                st.write("Inserta un comentario...")
    else:
        st.write("Inserta un comentario...")

