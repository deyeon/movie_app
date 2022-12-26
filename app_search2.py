import streamlit as st
import pandas as pd
import numpy as np

def run_search_app2():
    df=pd.read_csv('data/Best Movies Netflix.csv')
    df.set_index('index',inplace=True)
    df.isna().sum()

    st.subheader('영화를 검색해보세요!')

    c_list1=sorted(df['RELEASE_YEAR'].value_counts().index)
    selected_list1=st.selectbox('연도를 선택하세요', c_list1)
    
    if selected_list1 == 1954:
        year= 1954
    elif selected_list1 == 1961:
        year = 1961
    elif selected_list1 == 1964:
        year = 1964
    elif selected_list1 == 1966:
        year = 1966
    elif selected_list1 == 1967:
        year = 1967
    elif selected_list1 == 1971:
        year = 1971
    elif selected_list1 == 1973:
        year = 1973
    elif selected_list1 == 1975:
        year = 1975
    elif selected_list1 == 1976:
        year = 1976
    elif selected_list1 == 1979:
        year = 1979
    elif selected_list1 == 1980:
        year = 1980
    elif selected_list1 == 1982:
        year = 1982
    elif selected_list1 == 1984:
        year = 1984
    elif selected_list1 == 1986:
        year = 1986
    elif selected_list1 == 1987:
        year = 1987
    elif selected_list1 == 1989:
        year = 1989
    elif selected_list1 == 1990:
        year = 1990
    elif selected_list1 == 1991:
        year = 1991
    elif selected_list1 == 1992:
        year = 1992
    elif selected_list1 == 1993:
        year = 1993
    elif selected_list1 == 1994:
        year = 1994
    elif selected_list1 == 1995:
        year = 1995
    elif selected_list1 == 1996:
        year = 1996
    elif selected_list1 == 1997:
        year = 1997
    elif selected_list1 == 1998:
        year = 1998
    elif selected_list1 == 1999:
        year = 1999
    elif selected_list1 == 2000:
        year = 2000
    elif selected_list1 == 2001:
        year = 2001
    elif selected_list1 == 2002:
        year = 2002
    elif selected_list1 == 2003:
        year = 2003
    elif selected_list1 == 2004:
        year = 2004
    elif selected_list1 == 2005:
        year = 2005
    elif selected_list1 == 2006:
        year = '2006'
    elif selected_list1 == 2007:
        year = 2007
    elif selected_list1 == 2008:
        year = 2008
    elif selected_list1 == 2009:
        year = 2009
    elif selected_list1 == 2010:
        year = 2010
    elif selected_list1 == 2011:
        year = 2011
    elif selected_list1 == 2012:
        year = 2012
    elif selected_list1 == 2013:
        year = 2013
    elif selected_list1 == 2014:
        year = 2014
    elif selected_list1 == 2015:
        year = 2015
    elif selected_list1 == 2016:
        year = 2016
    elif selected_list1 == 2017:
        year = 2017
    elif selected_list1 == 2018:
        year = 2018
    elif selected_list1 == 2019:
        year = 2019
    elif selected_list1 == 2020:
        year = 2020
    elif selected_list1 == 2021:
        year = 2021
    elif selected_list1 == 2022:
        year = 2022

    
       
    c_list3=['액션','애니메이션','코메디','범죄','다큐멘터리','드라마','판타지','공포','뮤지컬','로맨스','공상,sf','스포츠','스릴러','전쟁','서부']
    selected_list3=st.selectbox('장르를 선택하세요', c_list3)
    if selected_list3 == '액션' :
        genre = 'action'
    elif selected_list3 == '애니메이션' :
        genre = 'animation'
    elif selected_list3 == '코메디':
        genre = 'comedy'
    elif selected_list3 == '범죄':
        genre = 'crime'
    elif selected_list3 == '다큐멘터리':
        genre = 'documentary'
    elif selected_list3 == '드라마':
        genre = 'drama'
    elif selected_list3 == '판타지':
        genre = 'fantasy'
    elif selected_list3 == '공포':
        genre = 'horror'
    elif selected_list3 == '뮤지컬':
        genre = 'musical'
    elif selected_list3 == '로맨스':
        genre = 'romance'
    elif selected_list3 == '공상,sf':
        genre = 'scifi'
    elif selected_list3 == '스포츠':
        genre = 'sports'
    elif selected_list3 == '전쟁':
        genre = 'war'
    elif selected_list3 == '서부':
        genre = 'western'
    
    c_list4=['아르헨티나','호주','벨기에','브라질','캐나다','콩고','중국','독일','덴마크','스페인','프랑스','영국','홍콩','헝가리','인도네시아','아일랜드','인도','이탈리아','일본','캄보디아','대한민국','리투아니아','말라위','멕시코','네덜란드','노르웨이','뉴질랜드','폴란드','팔레스타인','태국','터키','우크라이나','미국','남아프리카공화국','(국가없음)']
    selected_list4=st.selectbox('국가를 선택하세요', c_list4)
    if selected_list4 == '아르헨티나' :
        nation ='AR'
    elif selected_list4 == '호주':
        nation ='AU'
    elif selected_list4 == '벨기에':
        nation ='BE'
    elif selected_list4 == '브라질':
        nation ='BR'
    elif selected_list4 == '캐나다':
        nation ='CA'
    elif selected_list4 == '콩고':
        nation ='CD'
    elif selected_list4 == '중국':
        nation ='CN'
    elif selected_list4 == '독일':
        nation ='DE'
    elif selected_list4 == '덴마크':
        nation ='DK'
    elif selected_list4 == '스페인':
        nation ='ES'
    elif selected_list4 == '프랑스':
        nation ='FR'
    elif selected_list4 == '영국':
        nation ='GB'
    elif selected_list4 == '홍콩':
        nation ='HK'
    elif selected_list4 == '헝가리':
        nation ='HU'
    elif selected_list4 == '인도네시아':
        nation ='ID'
    elif selected_list4 == '아일랜드':
        nation ='IE'
    elif selected_list4 == '인도':
        nation ='IN'
    elif selected_list4 == '이탈리아':
        nation ='IT'
    elif selected_list4 == '일본':
        nation ='JP'
    elif selected_list4 == '캄보디아':
        nation ='KH'
    elif selected_list4 == '대한민국':
        nation ='KR'
    elif selected_list4 == '리투아니아':
        nation ='LT'
    elif selected_list4 == '말라위':
        nation ='MW'
    elif selected_list4 == '멕시코':
        nation ='MX'
    elif selected_list4 == '네덜란드':
        nation ='NL'
    elif selected_list4 == '노르웨이':
        nation ='NO'
    elif selected_list4 == '뉴질랜드':
        nation ='NZ'
    elif selected_list4 == '폴란드':
        nation ='PL'
    elif selected_list4 == '팔레스타인':
        nation ='PS'
    elif selected_list4 == '태국':
        nation ='TH'
    elif selected_list4 == '터키':
        nation ='TR'
    elif selected_list4 == '우크라이나':
        nation ='UA'
    elif selected_list4 == '미국':
        nation ='US'
    elif selected_list4 == '남아프리카공화국':
        nation ='ZA'
    elif selected_list4 == '(국가없음)':
        nation ='XX'
    




    
    
    

    
    
    
    
    star = st.slider('평점을 선택하세요',6.9,9.0,step=0.1)

    # c_list2=sorted(df['SCORE'].value_counts().index)
    # selected_list2=st.selectbox('평점(10점 만점)', c_list2)
    # if selected_list2 == 6.9:
    #     star = 6.9
    # elif selected_list2 == 7.0:
    #     star = 7.0
    # elif selected_list2 == 7.0:
    #     star = 7.0
    

    
    
    
    
    
    
    
    
    
       
    
    show_df=df.loc[(df['RELEASE_YEAR']==year)|(df['SCORE']==star)|(df['MAIN_GENRE']==genre)|(df['MAIN_PRODUCTION']==nation),]
    st.dataframe(show_df)


    
    