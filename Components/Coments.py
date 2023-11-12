import streamlit as st
import time


def convert_time(time):
    # funcion que trata el time
    time = time.split("T")
    time = time[0].split("-")
    time = time[2] + "-" + time[1] + "-" + time[0]
  

    return time

def Card_New(item_json, result):
    
    name = item_json['snippet']['topLevelComment']['snippet']['authorDisplayName']
    text = item_json['snippet']['topLevelComment']['snippet']['textDisplay']
    image = item_json['snippet']['topLevelComment']['snippet']['authorProfileImageUrl']
    result_value = result[0]['label']
    time = item_json['snippet']['topLevelComment']['snippet']['publishedAt']
    time = convert_time(time)

    st.markdown(
        """
        <style>  
        .section_name {
           border: 1px solid white;
            width: 100%;
            height: 100%;
            padding: 11px;
            border-radius: 12px;
            background: #ffffff1c;
            box-shadow: rgba(0, 0, 0, 0.3) 0px 19px 38px, rgba(0, 0, 0, 0.22) 0px 15px 12px;
            margin-top: 21px;
        }
        .Card-comment {
        width: 100%;
        height: 40%;
        display: flex;   
        }
        .img-content {
            width: 18%;
            display: flex;
            justify-content: center;
            align-items: center;
        }
        .content_text {
            width: 82%;
        }
        .image_person {
            border-radius: 50%;
            width: 75px;
            height: 75px;
        }
        .name_username {
            flex-direction: row;
            height: 40%;
            display: flex;
            align-items: flex-end;
        }
        .text_name_value {
            padding: 0px !important;
            margin: 0px !important;
            font-size: 20px;    
        }
        .from_text {
            background: #80808047;
            border-radius: 13px !important;
            padding: 0px 10px !important;
            margin: 0px !important;
            font-size: 20px;   
            color: #9fa4aa; 
        }
        .prediction_positive {
            width: 133px;
            height: 20px;
            position: absolute;
            right: 14px;
            top: 1px;
            background: #0000ff4d !important;
            border-radius: 10px 10px 0px 0px;
            display: flex;
            justify-content: center;
        }
        .prediction_negative {
            width: 133px;
            height: 20px;
            position: absolute;
            right: 14px;
            top: 1px;
            background: #ff000047 !important;
            border-radius: 10px 10px 0px 0px;
            display: flex;
            justify-content: center;
        }
        </style>
    """, unsafe_allow_html=True)

    st.write(
    f"""
        <section class="section_name">
            <div class="prediction">
                <span class="{"prediction_positive" if result_value == "POSITIVE" else "prediction_negative"}">{result_value}</span>
            </div>
            <div class="Card-comment">
                <div class="img-content">
                    <img src="{image}" alt="imagen" class="image_person">  
                </div>
                <div class="content_text">
                    <div class="name_username">
                        <p class="text_name_value" >  {name}</p>
                        <p class="from_text">{time}</p>
                    </div>
                    <div class="text">
                        <p>{text}</p>
                    </div>
                </div>
            </div>
        </section>

    """, unsafe_allow_html=True
)
