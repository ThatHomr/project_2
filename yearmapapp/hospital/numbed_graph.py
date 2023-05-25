import pandas as pd
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots

class Num_bed_View :

    def __init__(self) :
        self.initDataFrame()

    def initDataFrame(self) : 
        file_path = "./yearmapapp/hospital/병상수_마커.csv"
        self.data = pd.read_csv(file_path)
        self.data.drop(columns=['Unnamed: 0'], inplace=True)

    def setYearDataFrame(self, area_data) :
        area = area_data

        self.df_ver = self.data.query('시도 == @area')
        self.df_data = self.df_ver[['연도', '사용량', '병상수']]
        self.df_data_test = self.df_data.to_dict(orient='records')

        return self.df_data

    def initVisualization(self, data) :
        trace1 = go.Scatter(x = data["연도"], 
                            y = data["사용량"],
                            name='전력 사용량')

        trace2 = go.Scatter(x = data["연도"], 
                            y = data["병상수"], 
                            name='병상수', 
                            yaxis='y2')
        
        # 하나의 x축과 두 개의 y축으로 레이아웃 생성
        layout = go.Layout(title='전력 사용량 VS 병상수',
                            yaxis=dict(title='전력 사용량'),
                            yaxis2=dict(title='병상수',overlaying='y',side='right'))

        self.fig = go.Figure(data=[trace1, trace2], layout=layout)

        return self.fig.to_html()
