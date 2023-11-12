import streamlit as st 
from Scrapper.predict import predict_page
from Scrapper.Youtube import youtube_page


page = st.sidebar.selectbox("Selecciona una página", ["Predict-Comments", "Scrapping"])
# si la sección es "Visualización de Datos"


if page == "Predict-Comments":
    # Título de la app
    st.write("""
    <div style="display: flex; justify-content: center; align-items: center; margin: 0px 0px 30px 0px;">
        <h1 style="font-size: 45px; text-align: center; border-bottom: 1px solid red;">Youtube Predict Comments</h1>
    </div>""", unsafe_allow_html=True)

    # IMAGE
    st.write("""
        <div style="display: flex; justify-content: center; align-items: center; box-shadow: rgba(0, 0, 0, 0.25) 0px 14px 28px, rgba(0, 0, 0, 0.22) 0px 10px 10px; padding: 10px;">
            <img src="https://fs-prod-cdn.nintendo-europe.com/media/images/10_share_images/games_15/nintendo_switch_download_software_1/H2x1_NSwitchDS_YouTube_image1280w.jpg" alt="aereolina" width="700" style="margin: 10px 0px; border-radius: 6px;">
        </div>""", unsafe_allow_html=True)



    # label + input
    value_comment = st.text_area("", height=25, placeholder="Inserte un comentario...", key="comment_preddict")
    # button created
    button_preddict = st.button("Predict", key="predict_button",  type="primary", use_container_width=True)

    if button_preddict:
        predict_page(value_comment)

elif page == "Scrapping":
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

        # TITULO
    st.write("""
            <div style="display: flex; justify-content: center; align-items: center; margin: 0px 0px 30px 0px;">
                <h1 style="font-size: 45px; text-align: center; border-bottom: 1px solid white;">Youtube</h1>
            </div>""", unsafe_allow_html=True)

    # IMAGE
    st.write("""
            <div style="display: flex; justify-content: center; align-items: center; box-shadow: rgba(0, 0, 0, 0.25) 0px 14px 28px, rgba(0, 0, 0, 0.22) 0px 10px 10px; padding: 10px;">
                <img src="https://media2.giphy.com/media/LP62GF82YvcuOuFJRD/giphy.gif?cid=ecf05e47hsutrc15t05in0wrr7a9veckswprb9xikrzm8a6f&ep=v1_gifs_search&rid=giphy.gif&ct=g" alt="aereolina" width="300" style="margin: 10px 0px; border-radius: 6px;">
            </div>""", unsafe_allow_html=True)

    # TEXT AREA
    value = st.text_area("", height=25, placeholder="Inserta un link de un video de youtube", key="youtube")

    # BUTTON centramos el button
    button = st.button("Scrappear", key="youtube_button", type="primary", use_container_width=True)
    if button:
        try:
            youtube_page(value)
        except:
            st.write("Inserta un link de un video de youtube")