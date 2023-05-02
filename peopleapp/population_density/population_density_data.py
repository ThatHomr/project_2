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
        file_path = "./peopleapp/population_density/전력량_인구밀도_마커.csv"
        self.pop_data = pd.read_csv(file_path)
        self.pop_data.drop(columns=['Unnamed: 0'], inplace=True)

    # 특정 년 지역 받아와서 데이터 프레임 만들기
    def setYearDataFrame(self, year_data, area_data) :
        year = year_data
        area = area_data
        
        self.df_ver = self.pop_data.query('연도 == @year & 시도 == @area')
        self.df_data = self.df_ver[['월', '사용량', '인구밀도']]
        self.df_data_test = self.df_data.to_dict(orient='records')
        
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
    def initVisualization(self, year_data, area_data) :   
        # 첫번째 x축을 기준으로 그래프 생성
        trace1 = go.Scatter(
            x = self.df_data["월"],
            y = self.df_data["사용량"],
            name='전력 사용량'
        )
        
        # 두번째 x축을 기준으로 그래프 생성
        trace2 = go.Scatter(
            x = self.df_data["월"],
            y = self.df_data["인구밀도"],
            name='인구밀도',
            yaxis='y2'
        )
        
        # 하나의 x축과 두 개의 y축으로 레이아웃 생성
        layout = go.Layout(
            title='전력 사용량 VS 인구밀도',
            yaxis=dict(
                title='전력 사용량'
            ),
            yaxis2=dict(
                title='인구밀도',
                overlaying='y',
                side='right'
            )
        )

        # fig = make_subplots(
        #     rows=2, cols=2,
        #     start_cell="bottom-left",  # 시작 위치를 바꿀 수 있음
        #     subplot_titles=("Plot 1", "Plot 2", "Plot 3", "Plot 4") # 각 Subplot 별 subtitle 넣기
        # )
        
        # 레이아웃 조합 후 그래프 작성
        self.fig = go.Figure(data=[trace1, trace2], layout=layout)
        
        return self.fig.to_html()
