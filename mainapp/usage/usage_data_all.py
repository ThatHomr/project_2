### 데이터프레임을 사용할 수 있는 라이브러리 불러들이기
import pandas as pd
### 시각화 라이브러리 불러들이기
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

class Data_all_View :

    ### 클래스 생성 시점에 아래 함수들 순서대로 호출 실행(저장까지)
    def __init__(self) :
        self.initDataFrame()

    ### 데이터 읽어들이기
    def initDataFrame(self) :
        file_path = "./mainapp/usage/전력 사용량 14차.csv"
        self.usage_data = pd.read_csv(file_path)
        self.usage_data.drop(columns=['Unnamed: 0'], inplace=True)

    # 특정 년 받아와서 데이터 프레임 만들기
    def setYearDataFrame(self, area_data) :
        area = area_data
        
        self.df_ver = self.usage_data.query('시도 == @area')
        self.df_data = self.df_ver[['년월', '사용량']]
        self.df_data_test = self.df_data.to_dict(orient='records')
        return self.df_data
    
    ###  그래프 그리기
    def initVisualization(self, data) :
        # x, y 데이터로 그래프 생성
        trace = go.Scattergl(
            x=data['년월'],
            y=data['사용량'],
            mode='lines',
            line=dict(
                color='blue'
            ),
            name='전력 사용량'
        )

        # 레이아웃 생성
        layout = go.Layout(
            title='전력 사용량',
            xaxis=dict(
                title='년월',
                type='date'
            ),
            yaxis=dict(
                title='사용량'
            )
        )
        
        # 레이아웃 조합 후 그래프 작성
        fig = go.Figure(data=[trace], layout=layout)
        
        return fig.to_html()
