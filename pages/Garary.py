import streamlit as st
from PIL import Image
import pandas as pd

st.title('ギャラリー')

col1, col2, col3= st.columns(3)

with col1:
    image = Image.open('./data/ギャラリー1.jpg')
    st.image(image,width=200)
    st.text('東京駅丸の内広場')
with col2:
    image = Image.open('./data/ギャラリー2.jpg')
    st.image(image,width=200)
    st.text('自作コロッケ完成')
with col3:
    image = Image.open('./data/ギャラリー3.jpg')
    st.image(image,width=200)
    st.text('赤穂市坂越の海岸')
