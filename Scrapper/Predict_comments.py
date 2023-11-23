import streamlit as st
from transformers import pipeline
from transformers import DistilBertTokenizer, DistilBertForSequenceClassification
from torch.nn import Softmax
import torch
from googletrans import Translator
import joblib
import regex as re
import spacy
from spacy.tokenizer import Tokenizer
from spacy.lang.en import English

# Instanciamos el modelo
nlp_english = spacy.load("en_core_web_sm")

# FUNCION QUE SE ENCARGA DE PREDECIR EL COMENTARIO MODELO DE HUGGING FACE
def predict_comments(value_contents):
    if value_contents:
            classifier = pipeline("text-classification", model="nlptown/bert-base-multilingual-uncased-sentiment")
            # classifier = pipeline("text-classification")
            # result = classifier(value_contents)
            result = classifier(value_contents)
    return result 

# Funcion para cargar el modelo propio
def modelo_propio(text):
    loaded_model = joblib.load("C:/Users/Alexis/Desktop/proyectos/NLP_detector_mensajes_odio/Scrapper/modelo_entrenado.joblib")
    predic = loaded_model.predict([text])
    if predic == 0:
        return {"label": "POSITIVE", "score": 0.9999998807907104}
    else:
        return {"label": "NEGATIVE", "score": 0.9999998807907104}

# Funcion para traducir el texto
def translate_to_english(text: str):
    try:
        translator = Translator()
        translation = translator.translate(text, dest='en')
        return translation.text
    except Exception as e:
        return text

# Funcion para limpiar el texto
def limpieza_regex(text):
  text = str(text).lower() # Convierte el texto a minúsculas
  text = re.sub('\n', '', text)  # Elimina saltos de línea
  text = re.sub('\w*\d\w*', '', text)  # Elimina palabras que contienen números
  text = re.sub('\[|\]', '', text) # Elimina corchetes
  text = re.sub(r"\@w+|\#w+",'',text)  # Elimina menciones y hashtags de redes sociales
  text = re.sub('https?://\S+|www\.\S+', '', text)  # Elimina URLs que comiencen con http, https o www
  text = re.sub('<.*?>+', '', text)  # Elimina etiquetas HTML
  text = re.sub(r"[^\w\s]",'',text)  # Elimina caracteres no alfanuméricos
  text = re.sub('\xa0', '', text)  # Elimina el carácter \xa0
  text = re.sub(' +', ' ', text)  # Reemplaza múltiples espacios por uno solo
  text = text.strip() # Elimina espacios antes y despues
  return text

# Funcion para eliminar Stopwords
def eliminar_stop_words(text):
    doc = nlp_english(text)
    tokens = [token.text for token in doc if not token.is_stop]
    return " ".join(token for token in tokens)

# Funcion para lematizar los tokens
def lematizar_tokens(text):
    doc = nlp_english(text)
    tokens = [token.lemma_ for token in doc]
    return " ".join(tokens)

# FUNCION QUE SE ENCARGA DE PROCESAR EL TEXTO 
def process_text(text):
    text = limpieza_regex(text)
    text = eliminar_stop_words(text)
    text = lematizar_tokens(text)
    return text