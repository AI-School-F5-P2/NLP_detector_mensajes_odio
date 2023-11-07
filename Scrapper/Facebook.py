# importamos las librerias
import streamlit as st  
from facebook_scraper import get_posts
from transformers import pipeline



classifier = pipeline("text-classification")


st.markdown(
    """
    <style>
    .card {
  position: relative;
  background-color: #30344c;
  padding: 1em;
  z-index: 5;
  box-shadow: 4px 4px 20px rgba(0, 0, 0, 0.3);
  border-radius: 10px;
  max-width: 800px;
  transition: 200ms ease-in-out;
  margin: 15px auto;
}

.username {
  color: #C6E1ED;
  font-size: 0.85em;
  font-weight: 600;
}

.body {
  display: flex;
  flex-direction: column;
}

.body .text {
  margin: 0 10px 0 0;
  white-space: pre-line;
  color: #c0c3d7;
  font-weight: 400;
  line-height: 1.5;
  margin-bottom: 4px;
}

.footer {
  position: relative;
  width: 100%;
  color: #9fa4aa;
  font-size: 12px;
  display: flex;
  align-items: center;
  justify-content: space-between;
  border: none;
  margin-top: 10px;
}

.footer div {
  margin-right: 1rem;
  height: 20px;
  display: flex;
  align-items: center;
  cursor: pointer;
}

.footer svg {
  margin-right: 5px;
  height: 100%;
  stroke: #9fa4aa;
}

.viewer span {
  height: 20px;
  width: 20px;
  background-color: rgb(28, 117, 219);
  margin-right: -6px;
  border-radius: 50%;
  border: 1px solid #fff;
  display: grid;
  align-items: center;
  text-align: center;
  font-weight: bold;
  font-size: 8px;
  color: #fff;
  padding: 2px;
}

.viewer span svg {
  stroke: #fff;
}
    </style>
    """,
        unsafe_allow_html=True
    )


# TITULO
st.write("""
        <div style="display: flex; justify-content: center; align-items: center; margin: 0px 0px 30px 0px;">
            <h1 style="font-size: 45px; text-align: center; border-bottom: 1px solid white;">Facebook</h1>
        </div>""", unsafe_allow_html=True)

# IMAGE
st.write("""
        <div style="display: flex; justify-content: center; align-items: center; box-shadow: rgba(0, 0, 0, 0.25) 0px 14px 28px, rgba(0, 0, 0, 0.22) 0px 10px 10px; padding: 10px;">
            <img src="https://media3.giphy.com/media/l41lX2yEwhnD6QrLi/200w.webp?cid=ecf05e47a3yssrhj5ohyz35ojl03q304i6klrnnmd0qlaahp&ep=v1_gifs_search&rid=200w.webp&ct=g" alt="aereolina" width="300" style="margin: 10px 0px; border-radius: 6px;">
        </div>""", unsafe_allow_html=True)

# TEXT AREA
value = st.text_area("", height=25, placeholder="inserte el link de la pagina de Facebook con formato groups/012345678", key="facebook")

# BUTTON centramos el button
button = st.button("Scrappear", key="facebook_button")

if button:
    try:
        if value:
            st.write(value)
            for post in get_posts(value, pages=10):
                result = classifier(post['text'])
                st.write(f"""
            
                    <div class="card">                    
                        <div class="body">
                            <p class="text">{post['text']}</p>
                            <span class="username">from: {post['username']}</span>
                            <span class="result">result:: {result}</span>
                        </div>                
                    </div>""", unsafe_allow_html=True)

    except Exception as e:
        st.error(f"Error al raspar los datos: {e}")

