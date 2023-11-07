import tweepy
import streamlit as st
# Define tus claves y tokens de acceso
consumer_key = 'nnopckmmYpUQ4P947hQYF71jd'
consumer_secret = '65Qwm0O1b1o2YrUEq636tVI542bNP0vZ1zyj2LVanJ7cWy189K'
access_token = '1606341179318177795-pwQlsFeSCJW28y4YwUqYxkByhfijit'
access_token_secret = 'C3WOOaoGou1gL5cHFPCHgV9n0DvrazysDEnn45F4SDuBY'

# Autenticación
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Inicializa la API de Twitter
api = tweepy.API(auth)

# ID del tweet que deseas obtener
tweet_id = 'ID_DEL_TWEET'


# TITULO
st.write("""
        <div style="display: flex; justify-content: center; align-items: center; margin: 0px 0px 30px 0px;">
            <h1 style="font-size: 45px; text-align: center; border-bottom: 1px solid white;">Facebook</h1>
        </div>""", unsafe_allow_html=True)

# IMAGE
st.write("""
        <div style="display: flex; justify-content: center; align-items: center; box-shadow: rgba(0, 0, 0, 0.25) 0px 14px 28px, rgba(0, 0, 0, 0.22) 0px 10px 10px; padding: 10px;">
            <img src="https://media3.giphy.com/media/MNa0HKdhc3SGQ/200w.webp?cid=ecf05e47wrrybh1wf07vmlxp4vin4rm9myvsbyrzec4peqaq&ep=v1_gifs_search&rid=200w.webp&ct=g" alt="aereolina" width="300" style="margin: 10px 0px; border-radius: 6px;">
        </div>""", unsafe_allow_html=True)

# TEXT AREA
value = st.text_area("", height=25, placeholder="inserte el link de la pagina de Facebook con formato groups/012345678", key="twitter")

# BUTTON centramos el button
button = st.button("Scrappear", key="twitter_button")
if button:
    tweet = api.get_status(value, tweet_mode='extended')
    st.write(tweet)
        # print(f'Tweet: {tweet.full_text}')
        # print(f'Usuario: {tweet.user.screen_name}')
        # print(f'Fecha: {tweet.created_at}')
