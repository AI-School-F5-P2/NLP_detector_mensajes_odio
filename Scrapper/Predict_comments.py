import streamlit as st
from transformers import pipeline

def predict_comments(value_contents):
    result = None

    if value_contents:
        # Muestra un spinner mientras se realiza la predicción
       
            classifier = pipeline("text-classification")
            result = classifier(value_contents)



    return result 

