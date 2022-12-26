import streamlit as st
from app_home import run_home_app
from app_Data import run_data_app
from app_Chart import run_chart_app
from app_search1 import run_search_app1
from app_search2 import run_search_app2

def main():
    
    st.title('넷플릭스 영화 데이터 분석앱!')

    menu = ['Home','Data','Chart','Search']
    
    choice = st.sidebar.selectbox('메뉴',menu)
    
    
    if choice == 'Home':
        run_home_app()
    elif choice == 'Data':
        run_data_app()
    elif choice == 'Chart':
        run_chart_app()
    elif choice == 'Search':
        status3 =st.sidebar.radio('설정을 선택하세요',['제목으로 검색','조건으로 검색'])
        if status3 == '제목으로 검색':
            run_search_app1()
        
        elif status3 == '조건으로 검색':
            run_search_app2()




if __name__ == '__main__':
    main()