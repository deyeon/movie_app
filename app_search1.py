import streamlit as st
import pandas as pd
import numpy as np

def run_search_app1():
    df=pd.read_csv('data/Best Movies Netflix.csv')
    df.set_index('index',inplace=True)
    df.isna().sum()

    st.subheader('영화를 검색해보세요!')


    movie_word = st.text_input('영화 이름 입력(영어로)')

    st.text(movie_word)

    df_movie=df[df['TITLE'].str.contains(movie_word,case=False)]

    if len(movie_word)!= 0:
        st.dataframe(df_movie)

    else:
        st.info("영화를 검색해보세요")