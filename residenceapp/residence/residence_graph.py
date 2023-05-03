### 데이터프레임을 사용할 수 있는 라이브러리 불러들이기
import pandas as pd
### 시각화 라이브러리 불러들이기
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

class Data_View :

    ### 클래스 생성 시점에 아래 함수들 순서대로 호출 실행(저장까지)
    def __init__(self) :
        self.initDataFrame()

    ### 데이터 읽어들이기
    def initDataFrame(self) :
        file_path = "./residenceapp/residence/전력량_주택_마커.csv"
        self.usage_data = pd.read_csv(file_path)
        self.usage_data.drop(columns=['Unnamed: 0'], inplace=True)

    # 특정 년 받아와서 데이터 프레임 만들기
    def setYearDataFrame(self, year_data, area_data) :
        year = year_data
        area = area_data
        
        self.df_ver = self.usage_data.query('연도 == @year & 시도 == @area')
        self.df_data = self.df_ver[['월', '사용량', '주택가격변동률', '위도', '경도']]
        self.df_data_test = self.df_data.to_dict(orient='records')
        return self.df_data
        
    # ### 특정년 리스트 만들기
    # def setYearList(self, year_data) :
    #     self.year = year_data
    #     if self.year is "ERROR":
    #         self.year = 2021
    #     self.year = int(self.year)

    #     self.df_ver = self.usage_data.query('연도 == @year')
    #     year_list = []
    #     for item in self.df.ver :
    #         year_list.append(item['사용량'])
    #     return year_list
    
    ###  그래프 그리기
    def initVisualization(self, data) :
        # 첫번째 x축을 기준으로 그래프 생성
        trace1 = go.Scatter(
            x = data["월"],
            y = data["사용량"],
            name='전력 사용량'
        )
        # 두번째 x축을 기준으로 그래프 생성
        trace2 = go.Scatter(
            x = data["월"],
            y = data["주택가격변동률"],
            name='주택가격변동률'
        )
        
        # 하나의 x축과 두 개의 y축으로 레이아웃 생성
        layout = go.Layout(
            title='전력 사용량',
            yaxis=dict(
                title='전력 사용량'
            ),
            yaxis2=dict(
                title='주택가격변동률',
                overlaying='y',
                side='right'
            )
        )
        
        # 레이아웃 조합 후 그래프 작성
        fig = go.Figure(data=[trace1, trace2], layout=layout)
        
        return fig.to_html()
