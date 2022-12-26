import streamlit as st


def run_home_app():
    st.markdown('NETFLIX 월드 베스트 영화 데이터 분석 앱')
    st.text('netflix에서 서비스하는 영화의 데이터입니다.')
    st.text('데이터 메뉴에서 각 컬럼별로 데이터의 최대/최소 데이터를 보실수 있습니다.')
    st.text('차트 메뉴에서 각 컬럼별로 히스토그램과 파이차트를 보실수 있고 컬럼별로 어떤 상관관계가 있는지 히트맵 을 통해 한눈에 보실수 있습니다.')
    st.text('검색 메뉴에서 영화제목별로 조건별로 영화를 검색하실수 있습니다.')

    st.markdown('위에 화살표를 누르시면 메뉴를 보실수 있습니다.')
    st.image("https://cdn.pixabay.com/photo/2020/09/14/17/45/tv-5571609_960_720.jpg")