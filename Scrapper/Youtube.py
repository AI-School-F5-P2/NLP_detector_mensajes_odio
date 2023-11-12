import googleapiclient.discovery
import streamlit as st
import re
from Components.Coments import Card_New
from Scrapper.Predict_comments import predict_comments

# Clave de la API de YouTube
api_key = 'AIzaSyBC6lNJ4taKhfAZ4dxGJfLmTapODsS6PI0'

def youtube_page(value: str):
  
    # Utiliza una expresión regular para encontrar el ID del video
    match = re.search(r'(?<=v=)[\w-]+', value)
    if match:
        video_id = match.group()

    #st.write(video_id)
    # Inicializar el servicio de YouTube
    youtube = googleapiclient.discovery.build('youtube', 'v3', developerKey=api_key)
    
    comentarios = []
    next_page_token = None
    try:
        while True:
            results = youtube.commentThreads().list(
                part='snippet',
                videoId=video_id,
                textFormat='plainText',
                pageToken=next_page_token
            ).execute()

            for item in results['items']:
                comentario = item['snippet']['topLevelComment']['snippet']['textDisplay']
                result = predict_comments(comentario)
                Card_New(item, result)

            next_page_token = results.get('nextPageToken')

            if not next_page_token:
                break
    except Exception as e:
        st.write(e)