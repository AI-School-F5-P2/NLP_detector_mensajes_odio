import streamlit as st
from transformers import pipeline
from transformers import DistilBertTokenizer, DistilBertForSequenceClassification
from torch.nn import Softmax
import torch

def predict_comments(value_contents):
    result = None
    if value_contents:
            classifier = pipeline("text-classification")
            result = classifier(value_contents)
    return result 

def predict_comments_v2(value_contents):

        # Cargar el modelo preentrenado y el tokenizador
        model_name = "distilbert-base-multilingual-cased"
        model = DistilBertForSequenceClassification.from_pretrained(model_name)
        tokenizer = DistilBertTokenizer.from_pretrained(model_name)

        # Agregar una capa de clasificación
        model.classifier = torch.nn.Linear(in_features=768, out_features=2)

        # Definir la función de softmax
        softmax = Softmax(dim=1)

        inputs = tokenizer(value_contents, return_tensors="pt")

        # Realizar la predicción
        with torch.no_grad():
                outputs = model(**inputs)

        # Aplicar la función de softmax a las predicciones
        probs = softmax(outputs.logits)

            # Obtener la probabilidad de la clase "toxic" (clase 1)
        toxicity_probability = probs[:, 1].item()

        return toxicity_probability

