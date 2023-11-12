import streamlit as st
import time
def CardComplement(text: str, accuracy:int, label: str):

    # convertimos el accuracy a porcentaje
    accuracy = accuracy * 100
    # lo redondeamos a 2 decimales
    accuracy = round(accuracy, 2)

   
            
    st.markdown(
        """
        <style>
        .img_like_or_dislike{
            width: 100%;
            }

        .card {
            border: 1px solid white;
            margin: 0 auto;
            width: 44em;
            height: 18.5em;
            background: #171717;
            transition: 1s ease-in-out;
            clip-path: polygon(30px 0%, 100% 0, 100% calc(100% - 30px), calc(100% - 30px) 100%, 0 100%, 0% 30px);
            border-top-right-radius: 20px;
            border-bottom-left-radius: 20px;
            display: flex;
            flex-direction: column;
            }

        .card span {
            font-weight: bold;
            color: red;
            text-align: center;
            display: block;
            font-size: 1em;
            }
        .span_2 {
           font-weight: bold;
            color: blue !important;
            text-align: center;
            display: block;
            font-size: 1em;
        }

        .card .info {
            font-weight: 400;
            color: white;
            display: block;
            text-align: center;
            font-size: 1.3em;
            margin: 1em;
            }

        .card .img {
            width: 4.8em;
            height: 4.8em;
            #background: white;
            border-radius: 15px;
            margin: auto;
            }
    
        .card .share {
            margin-top: 1em;
            display: flex;
            justify-content: center;
            gap: 1em;
            }

        .card a {
            color: white;
            transition: .4s ease-in-out;
            }

        .card a:hover {
            color: red;
            }

        .card button {
            padding: 0.8em 1.7em;
            display: block;
            margin: auto;
            border-radius: 25px;
            border: none;
            font-weight: bold;
            background: #ffffff;
            color: rgb(0, 0, 0);
            transition: .4s ease-in-out;
            }

        .card button:hover {
            background: red;
            color: white;
            cursor: pointer;
            }
        .rotate-scale-up-hor {
	        -webkit-animation: rotate-scale-up-hor 0.65s linear both;
	        animation: rotate-scale-up-hor 0.65s linear both;
            }
            @-webkit-keyframes rotate-scale-up-hor{0%{-webkit-transform:scale(1) rotateX(0);transform:scale(1) rotateX(0)}50%{-webkit-transform:scale(2) rotateX(-180deg);transform:scale(2) rotateX(-180deg)}100%{-webkit-transform:scale(1) rotateX(-360deg);transform:scale(1) rotateX(-360deg)}}@keyframes rotate-scale-up-hor{0%{-webkit-transform:scale(1) rotateX(0);transform:scale(1) rotateX(0)}50%{-webkit-transform:scale(2) rotateX(-180deg);transform:scale(2) rotateX(-180deg)}100%{-webkit-transform:scale(1) rotateX(-360deg);transform:scale(1) rotateX(-360deg)}}
        </style>
        """,
        unsafe_allow_html=True
    )
     

    st.write(f"""
        <div class="card">
            <div class="img">
             { '<img class="img_like_or_dislike rotate-scale-up-hor" src="https://cdn-icons-png.flaticon.com/128/566/566773.png" alt="like_or_dislike" />' if label == "POSITIVE" else '<img class="img_like_or_dislike rotate-scale-up-hor" src="https://cdn-icons-png.flaticon.com/128/4823/4823367.png" alt="like_or_dislike" />'}
             </div>
                <span class="{"span_2" if label == "POSITIVE" else ""}">{accuracy} %</span>
                <p class="info">{text}</p>
                 
               
       
             """, unsafe_allow_html=True)