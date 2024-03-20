import streamlit as st
from PIL import Image
import pandas as pd
# import matplotlib.pyplot as plt

st.title('木村 彰杜のホームページ')

col1, col2= st.columns(2)

with col1:
    image = Image.open('./data/自画像.jpg')
    st.image(image,width=300)

    st.subheader('☆プロフィール')
    st.text('木村 彰杜（きむら　あきと）\n'
            '生年月日 1999年10月20日\n'
            '血液型 B型')

    with st.form(key='profile_form'):
        name = st.text_input('名前')
        adress=st.text_input('住所')

        submit_btn = st.form_submit_button('送信')
        cancel_btn = st.form_submit_button('キャンセル')
        
        if submit_btn==True:
            st.text(f'ようこそ{name}さん！')
    

with col2:    
    st.subheader('最新研究情報')

    # df = pd.read_csv('./data/磁石3760G.csv')
    # fig = plt.figure(figsize=(5.5,5))
    # ax = fig.subplots()
    # ax.plot(df['distance[mm]'],df['magnetic field[G]'])
    # ax.set_xlabel('Distance mm')
    # ax.set_ylabel('Mangnetic field G')
    # st.pyplot(fig)

    st.text('表面磁束3760Gのネオジム磁石の磁場距離依存性\n'
            'を測定しました。')



