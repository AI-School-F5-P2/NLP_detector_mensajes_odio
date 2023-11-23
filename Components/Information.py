import streamlit as st


def title_markdown(text):
    st.sidebar.markdown(
        f"""
        <h1 style="font-size: 45px; text-align: center; border-bottom: 1px solid white; margin-bottom: 20px;"> {text} </h1>
        """, unsafe_allow_html=True
    )

def Information(total_negative: int, total_positive: int, item: dict, link_video: str):
    
    total_coments = total_negative + total_positive
    likes = item['snippet']['topLevelComment']['snippet']['likeCount']
    
    st.markdown(
        """
        <style>
        .card {
            height: auto !important;
            color: white;
            display: grid;
            grid-template-rows: 1fr 1fr;
            gap: 5px;
            overflow: visible;
            margin: 0 auto;
            box-shadow: rgba(50, 50, 93, 0.25) 0px 6px 12px -2px, rgba(0, 0, 0, 0.3) 0px 3px 7px -3px;
        }

        .card .item {
            border-radius: 10px;
            width: 100%;
            height: 100%;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
        }
        .item svg {
            width: 40px;
            height: 40px;
            margin-bottom: 7px;
        }

        .item--1 {
         background: #c7c7ff;
        }

        .item--2 {
        background: #ffd8be;
        }

        .item--3 {
        background: #a9ecbf;
        }

        .item--4 {
        background: #f3bbe1;
        }

        .quantity {
        font-size: 30px;
        font-weight: 600;
        }

        .text {
        font-size: 22px;
        font-family: inherit;
        font-weight: 600;
        }

        .text--1 {
        color: rgba(149,149,255,1);
        }

        .text--2 {
        color: rgba(252,161,71,1);
        }

        .text--3 {
        color: rgba(66,193,110,1);
        }

        .text--4 {
        color: rgba(220,91,183,1);
        }
        """, unsafe_allow_html=True
    )

    st.sidebar.write(
        """
        <h1 style="font-size: 45px; text-align: center; border-bottom: 1px solid white; margin-bottom: 20px;">Information</h1>
        """, unsafe_allow_html=True
    )

    st.sidebar.write(f"""
        <section style="display: flex; justify-content: center; align-items: center; box-shadow: rgba(0, 0, 0, 0.25) 0px 14px 28px, rgba(0, 0, 0, 0.22) 0px 10px 10px; padding: 10px; border-radius: 15px">
            <iframe width="560" height="315" src="https://www.youtube.com/embed/{link_video}" frameborder="0" allowfullscreen></iframe>'
        </section>""", unsafe_allow_html=True)

    st.sidebar.bar_chart({
                'Total de Comentarios': total_negative + total_positive,
                'Comentarios Positivos': total_positive,
                'Comentarios Negativos': total_negative
            })

    st.sidebar.write(
        f"""
        <section class="card">
            <div class="item item--1">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24"><path fill="none" d="M0 0h24v24H0z"></path><path d="M17 15.245v6.872a.5.5 0 0 1-.757.429L12 20l-4.243 2.546a.5.5 0 0 1-.757-.43v-6.87a8 8 0 1 1 10 0zm-8 1.173v3.05l3-1.8 3 1.8v-3.05A7.978 7.978 0 0 1 12 17a7.978 7.978 0 0 1-3-.582zM12 15a6 6 0 1 0 0-12 6 6 0 0 0 0 12z" fill="rgba(149,149,255,1)"></path></svg>
                <span class="quantity"> {total_coments} </span>
                <span class="text text--1"> Comments </span>
            </div>
            <div class="item item--2">
                <svg height="24" width="24" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="M0 0L24 0 24 24 0 24z" fill="none"></path><path fill="rgba(252,161,71,1)" d="M16 16c1.657 0 3 1.343 3 3s-1.343 3-3 3-3-1.343-3-3 1.343-3 3-3zM6 12c2.21 0 4 1.79 4 4s-1.79 4-4 4-4-1.79-4-4 1.79-4 4-4zm10 6c-.552 0-1 .448-1 1s.448 1 1 1 1-.448 1-1-.448-1-1-1zM6 14c-1.105 0-2 .895-2 2s.895 2 2 2 2-.895 2-2-.895-2-2-2zm8.5-12C17.538 2 20 4.462 20 7.5S17.538 13 14.5 13 9 10.538 9 7.5 11.462 2 14.5 2zm0 2C12.567 4 11 5.567 11 7.5s1.567 3.5 3.5 3.5S18 9.433 18 7.5 16.433 4 14.5 4z"></path></svg>  
                    <span class="quantity"> {likes} </span>
                <span class="text text--2"> Likes </span>
            </div>
            <div class="item item--3">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24"><path fill="none" d="M0 0h24v24H0z"></path><path d="M20.083 15.2l1.202.721a.5.5 0 0 1 0 .858l-8.77 5.262a1 1 0 0 1-1.03 0l-8.77-5.262a.5.5 0 0 1 0-.858l1.202-.721L12 20.05l8.083-4.85zm0-4.7l1.202.721a.5.5 0 0 1 0 .858L12 17.65l-9.285-5.571a.5.5 0 0 1 0-.858l1.202-.721L12 15.35l8.083-4.85zm-7.569-9.191l8.771 5.262a.5.5 0 0 1 0 .858L12 13 2.715 7.429a.5.5 0 0 1 0-.858l8.77-5.262a1 1 0 0 1 1.03 0zM12 3.332L5.887 7 12 10.668 18.113 7 12 3.332z" fill="rgba(66,193,110,1)"></path></svg>
                <span class="quantity"> {total_positive} </span>
                <span class="text text--3"> Positives </span>
            </div>
            <div class="item item--4">
                <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" width="24" height="24"><path fill="none" d="M0 0h24v24H0z"></path><path d="M12 20h8v2h-8C6.477 22 2 17.523 2 12S6.477 2 12 2s10 4.477 10 10a9.956 9.956 0 0 1-2 6h-2.708A8 8 0 1 0 12 20zm0-10a2 2 0 1 1 0-4 2 2 0 0 1 0 4zm-4 4a2 2 0 1 1 0-4 2 2 0 0 1 0 4zm8 0a2 2 0 1 1 0-4 2 2 0 0 1 0 4zm-4 4a2 2 0 1 1 0-4 2 2 0 0 1 0 4z" fill="rgba(220,91,183,1)"></path></svg>
                <span class="quantity"> {total_negative} </span>
                <span class="text text--4"> Negatives </span>
            </div>
        </section>
        """, unsafe_allow_html=True
    )