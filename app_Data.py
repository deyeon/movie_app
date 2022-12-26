import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb

def run_data_app():
    df=pd.read_csv('data/Best Movies Netflix.csv')
    df.set_index('index',inplace=True)
    df.isna().sum()

    st.subheader('데이터 요약')
    st.dataframe(df.describe())

    st.subheader('영화 별 최대/최소 데이터 확인하기')
    st.text("각 컬럼별로 최대/최소데이터를 확인 할수 있습니다.")
    column_list = ['평점(10만점)','투표수','재생시간(분)']
    
    selected_column=st.selectbox('컬럼을 선택하세요',column_list)

    if selected_column == '평점(10만점)':
        df_max1=df.loc[df['SCORE']==df['SCORE'].max(),]
        df_min1=df.loc[df['SCORE']==df['SCORE'].min(),]
        
        st.text('평점 최대')
        for i in range(0,len(df_max1)):
            st.text(df_max1['TITLE'].values[i])
        st.dataframe(df_max1)
        st.text('평점 최소')
        for i in range(0,len(df_min1)):
            st.text(df_min1['TITLE'].values[i])
        st.dataframe(df_min1)

    
    elif selected_column == '투표수':
        df_max2=df.loc[df['NUMBER_OF_VOTES']==df['NUMBER_OF_VOTES'].max(),]
        df_min2=df.loc[df['NUMBER_OF_VOTES']==df['NUMBER_OF_VOTES'].min(),]
        
        st.text('투표수 최대')
        for i in range(0,len(df_max2)):
            st.text(df_max2['TITLE'].values[i])
        st.dataframe(df_max2)
        st.text('투표수 최소')
        for i in range(0,len(df_min2)):
            st.text(df_min2['TITLE'].values[i])
        st.dataframe(df_min2)

    elif selected_column == '재생시간(분)':
        df_max3=df.loc[df['DURATION']==df['DURATION'].max(),]
        df_min3=df.loc[df['DURATION']==df['DURATION'].min(),]

        st.text('재생시간 최대')
        for i in range(0,len(df_max3)):
            st.text(df_max3['TITLE'].values[i])
        st.dataframe(df_max3)
        st.text('재생시간 최소')
        for i in range(0,len(df_min3)):
            st.text(df_min3['TITLE'].values[i])
        st.dataframe(df_min3)
    

