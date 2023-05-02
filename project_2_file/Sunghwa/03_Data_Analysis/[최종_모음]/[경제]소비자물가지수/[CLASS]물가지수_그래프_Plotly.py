### 데이터프레임을 사용할 수 있는 라이브러리 불러들이기
import pandas as pd
### 시각화 라이브러리 불러들이기
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

class CPI_Plotly :

    ### 클래스 생성 시점에 아래 함수들 순서대로 호출 실행(저장까지)
    def __init__(self) :
        self.initDataFrame()
        self.initVisualization()
        self.saveCPI_Fig()

    ### 데이터 읽어들이기
    def initDataFrame(self) :
        file_path = "기간_물가지수_전력소비량.csv"
        self.df_result = pd.read_csv(file_path)
        self.df_result.drop(columns=['Unnamed: 0'], inplace=True)

    
    def initVisualization(self) :
                
        trace1 = go.Scatter(
            x = self.df_result['기간'],
            y = self.df_result['전력소비량'],
            name='전력소비량'
        )
        
        trace2 = go.Scatter(
            x = self.df_result['기간'],
            y = self.df_result['물가지수'],
            name='소비자물가지수',
            yaxis='y2'
        )
        
        layout = go.Layout(
            title='전력소비량 대비 소비자물가지수',
            yaxis=dict(
                title='전력소비량'
            ),
            yaxis2=dict(
                title='소비자물가지수',
                overlaying='y',
                side='right'
            )
        )
        
        fig = go.Figure(data=[trace1, trace2], layout=layout)
       
        fig.show()

    ### 그래프 저장하기
    def saveCPI_Fig(self) :
        self.fig.savefig("./CPI_Plotly.png")
