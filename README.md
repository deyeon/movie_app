# movie_app
# 설명
  - netflix에서 서비스하는 영화의 데이터입니다.
  - 데이터 메뉴에서 각 컬럼별로 데이터의 최대/최소 데이터를 보실수 있습니다.
  - 차트 메뉴에서 각 컬럼별로 히스토그램과 파이차트를 보실수 있고 컬럼별로 어떤 상관관계가 있는지 히트맵
    을 통해 한눈에 보실수 있습니다.
   -검색 메뉴에서 영화제목별로 조건별로 영화를 검색하실수 있습니다.
   
# 진행과정

## 1. jupyter notebook에서 진행한 내용

  - csv형식의 데이터를 jupyter notebook으로 불러 작업하였습니다.
  - 데이터를 가공하는 과정에서 꼭 컬럼을 인덱싱으로 부르고 다시 데이터프레임에 저장하여 작업하였습니다.
  - 데이터의 상관분석과 차트를 만들어 진행하였습니다.
  - 인공지능파일을 pkl파일로 로컬에 보내서 작업하였습니다.

## 2. visual studio code 에서 작업

  - visual studio code에서 작업하여 streamlit라이브러리로 웹대시보드를 로컬에서 생성하여 작업하였습니다.
  - 영화를 제목별,조건별로 검색할수 있게 작업하였습니다.
  - 기존 plt차트에서 발전된 plotly차트를 사용하여 사용하는 유저가 차트에 데이터를 마우스만 올리면 볼 수 있게 하였습니다.
  - 상관분석을 통해 각 컬럼간에 데이터는 어떤 상관관계가 있는지 분석해보았고 분석 결과 데이터 별로 상관관계가 높지 않아서 인공지능은 사용하지 않았습니다.

## 3. github에서 작업 
  
   - visual studio code에서 작업한 내용을 githubdesktop를 이용해 push하여 github레포지토리로 보냈습니다.
   - github 레포지토리를 ec2에 clone하여 서버에서 웹대시보드를 실행하게 하였습니다. 
   - github Actions 기능을 이용하여 visual studio code에서 작업한 내용을 ec2서버에 바로 pull되어 수정사항을
     서버에 실시간으로 보낼수 있게 하였습니다.


## 4. aws ec2에서 작업

  - aws에서 ec2를 생성하여 프리 티어 서버를 생성하였습니다.
  - putty로 ec2에 접속하여 원격으로 작업하여 파이썬 환경을 구축하여 streamlit를 서버에서도 실행할 수 있게 하였습니다.
  - streamlit 웹대시보드를 서버 연결이 끊겨도 접속이 가능하게 하였습니다.
  - github 레포지토리에 있던 인공지능파일인 pkl파일을 ec2로 pull하여 서버에서도 인공지능이 실행될 수 있게 하였습니다. 
  
# 문제 해결
  - streamlit sidebar에서 search항목을 클릭하면 제목별,조건별로 검색할수 있게 라디오버튼을 만들려 했으나 sidebar 바깥으로 만들어져서
    streamlit 홈페이지에서 sidebar를 함수사이 입력하면된다는 점을 이해하고 라디오버튼을 sidebar에 정확히 적용하였습니다. 

# 스크린샷
   
# 데이터 레퍼런스

https://www.kaggle.com/datasets/thedevastator/the-ultimate-netflix-tv-shows-and-movies-dataset?resource=download&select=Best+Movies+Netflix.csv
