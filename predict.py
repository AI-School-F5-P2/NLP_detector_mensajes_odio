import streamlit as st
from transformers import pipeline

def predict_page(value_contents):
    result = None
    if value_contents:
        # classifier = pipeline("zero-shot-classification", model="joeddav/xlm-roberta-large-xnli")
        # candidate_labels = ["toxic", "severe_toxic", "obscene", "threat", "insult", "identity_hate"]
        # result = classifier(value_contents, candidate_labels)
        classifier = pipeline("text-classification")
        result = classifier(value_contents)
        st.write(result)
    else:
        st.write("Inserta un comentario...")