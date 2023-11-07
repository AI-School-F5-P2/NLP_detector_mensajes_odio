import os
import googleapiclient.discovery
import streamlit as st
import re



# Clave de la API de YouTube
api_key = 'AIzaSyBC6lNJ4taKhfAZ4dxGJfLmTapODsS6PI0'

# TITULO
st.write("""
        <div style="display: flex; justify-content: center; align-items: center; margin: 0px 0px 30px 0px;">
            <h1 style="font-size: 45px; text-align: center; border-bottom: 1px solid white;">Facebook</h1>
        </div>""", unsafe_allow_html=True)

# IMAGE
st.write("""
        <div style="display: flex; justify-content: center; align-items: center; box-shadow: rgba(0, 0, 0, 0.25) 0px 14px 28px, rgba(0, 0, 0, 0.22) 0px 10px 10px; padding: 10px;">
            <img src="https://media2.giphy.com/media/LP62GF82YvcuOuFJRD/giphy.gif?cid=ecf05e47hsutrc15t05in0wrr7a9veckswprb9xikrzm8a6f&ep=v1_gifs_search&rid=giphy.gif&ct=g" alt="aereolina" width="300" style="margin: 10px 0px; border-radius: 6px;">
        </div>""", unsafe_allow_html=True)


# TEXT AREA
value = st.text_area("", height=25, placeholder="inserte el link de la pagina de Facebook con formato groups/012345678", key="youtube")

# BUTTON centramos el button
button = st.button("Scrappear", key="youtube_button")

if button:

    # Utiliza una expresión regular para encontrar el ID del video
    match = re.search(r'(?<=v=)[\w-]+', value)
    if match:
        video_id = match.group()

    st.write(video_id)
    # Inicializar el servicio de YouTube
    youtube = googleapiclient.discovery.build('youtube', 'v3', developerKey=api_key)
        # Obtener los comentarios del video
    comentarios = []
    results = youtube.commentThreads().list(
            part='snippet',
            videoId=video_id,
            textFormat='plainText'
        ).execute()



    while results:
        for item in results['items']:
            
            comentario = item['snippet']['topLevelComment']['snippet']['textDisplay']
            # comentarios.append(comentario)
            # st.write(comentarios)
            st.write(f"""
            
                    <div class="card">                    
                        <div class="body">
                            <p class="text">{comentario}</p>
                        </div>                
                    </div>
                        """, unsafe_allow_html=True)
