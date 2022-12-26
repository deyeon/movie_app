import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sb

def run_chart_app():
    df=pd.read_csv('data/Best Movies Netflix.csv')
    df.set_index('index',inplace=True)


    df2 = df.loc[:,['RELEASE_YEAR', 'SCORE', 'DURATION']]
    status1 =st.radio('설정을 선택하세요',['연도','평점(10만점)','재생시간(분)'])
    st.text("각 기준별로 데이터가 얼마나 분포되어 있는지 나타낸 히스토그램입니다.")

    import plotly.express as px
    if status1 == '연도' :
        
        st.header('연도별 히스토그램')
        st.text("연도별로 데이터가 얼마나 분포되어 있는지 나타낸 히스토그램입니다.")
        fig1=px.histogram(df2,x=df2['RELEASE_YEAR'],nbins=20,color_discrete_sequence=["green"])
        fig1.update_layout(bargap=0.2,plot_bgcolor='#FFFFFF')
        st.plotly_chart(fig1)
    
    elif status1== '평점(10만점)' :

        st.header('평점별 히스토그램')
        st.text("평점별로 데이터가 얼마나 분포되어 있는지 나타낸 히스토그램입니다.")
        fig2=px.histogram(df2,x=df2['SCORE'],nbins=20,color_discrete_sequence=["green"])
        fig2.update_layout(bargap=0.2,plot_bgcolor='#FFFFFF')
        st.plotly_chart(fig2)

    elif status1== '재생시간(분)' :

        st.header('재생시간별 히스토그램')
        st.text("재생시간별로 데이터가 얼마나 분포되어 있는지 나타낸 히스토그램입니다.")
        fig3=px.histogram(df2,x=df2['DURATION'],nbins=20,color_discrete_sequence=["green"])
        fig3.update_layout(bargap=0.2,plot_bgcolor='#FFFFFF')
        st.plotly_chart(fig3)


    
    
    st.text("컬럼별로 데이터가 얼마나 분포되어 있는지 나타낸 파이차트입니다.")
    df3=df.loc[:,['SCORE','MAIN_GENRE','MAIN_PRODUCTION']]
    status2 =st.radio('설정을 선택하세요',['평점(10만점)','장르','제작사 국가'])
    
    if status2== '평점(10만점)' :
        fig4 = px.pie(df3,names=df3['SCORE'].value_counts().index,values=df3['SCORE'].value_counts(),title='평점별 파이차트')
        st.plotly_chart(fig4)
    
    elif status2== '장르':
        fig5 = px.pie(df3,names=df3['MAIN_GENRE'].value_counts().index,values=df3['MAIN_GENRE'].value_counts(),title='장르별 파이차트')
        st.plotly_chart(fig5)

    elif status2== '제작사 국가':
        fig6 = px.pie(df3,names=df3['MAIN_PRODUCTION'].value_counts().head(10).index,values=df3['MAIN_PRODUCTION'].value_counts().head(10),title='제작사 국가별 파이차트')
        st.plotly_chart(fig6)


    st.subheader('상관관계 분석')
    st.text("각 컬럼간의 상관관계를 분석하였습니다.")
    st.text("컬럼을 선택하여 상관분석을 할수 있습니다.")

    df4 = df.loc[:,['RELEASE_YEAR', 'SCORE', 'NUMBER_OF_VOTES', 'DURATION']]
    c_list = df4.columns
    selected_list=st.multiselect('상관분석을 하고싶은 컬럼을 선택하세요', c_list)

    if len(selected_list) >= 2:
            df_corr=df[selected_list].corr()
            fig7 = plt.figure()
            sb.heatmap(data=df_corr,annot=True,fmt='.2f',cmap='coolwarm',
            vmin = -1,vmax=1,linewidths=0.5)
            st.pyplot(fig7)



    