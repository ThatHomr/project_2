### 데이터프레임을 사용할 수 있는 라이브러리 불러들이기
import pandas as pd
### 시각화 라이브러리 불러들이기
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

class Tourist_Plotly :

    ### 클래스 생성 시점에 아래 함수들 순서대로 호출 실행(저장까지)
    def __init__(self) :
        self.initDataFrame()
        self.initVisualization()
        self.saveCPI_Fig()

    ### 데이터 읽어들이기
    def initDataFrame(self) :
        file_path = "기간_물가지수_전력소비량.csv"
        self.df = pd.read_csv(file_path)
        self.df.drop(columns=['Unnamed: 0'], inplace=True)

    
    def initVisualization(self) :
                
        trace1 = go.Scatter(
            x = self.df['기간'],
            y = self.df['전력소비량'],
            name='전력소비량'
        )

        # 두번째 x축을 기준으로 그래프 생성
        trace2 = go.Scatter(
            x = self.df['기간'],
            y = self.df['관광객'],
            name='관광목적 외래객 수',
            yaxis='y2'
        )

        # 하나의 x축과 두 개의 y축으로 레이아웃 생성
        layout = go.Layout(
            title='전력소비량 대비 관광목적 외래객 수',    
            yaxis=dict(
                title='전력소비량'
            ),
            yaxis2=dict(
                title='관광목적 외래객 수',
                overlaying='y',
                side='right'
            )
        )

        # 레이아웃 조합 후 그래프 작성
        fig = go.Figure(data=[trace1, trace2], layout=layout)

        # 그래프 표시
        fig.show()

    ### 그래프 저장하기
    def saveCPI_Fig(self) :
        self.fig.savefig("./Tourist_Plotly.png")