import streamlit as st
from transformers import pipeline
from Components.Loader import Loader
from Components.Card import Card
from Components.CardComplement import CardComplement

def predict_page(value_contents):
    result = None

    if value_contents:
        # Muestra un spinner mientras se realiza la predicción
        with st.spinner("Prediciendo..."):
            # Realiza la predicción
            classifier = pipeline("text-classification")
            result = classifier(value_contents)
            if result:
                st.write(result)
                #Card(value_contents, result[0]["score"], None)
                CardComplement(value_contents, result[0]["score"], result[0]["label"])
            else:
                st.write("Inserta un comentario...")

     
    else:
        st.write("Inserta un comentario...")

