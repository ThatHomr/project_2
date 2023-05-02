def pop_ele_graph(sido_select):

    import pandas as pd
    import plotly.graph_objs as go
    from plotly.subplots import make_subplots

    data = pd.read_csv('./2011~2022_시도별_인구수&전력사용량.csv')

    sido = sido_select
    data = data.query('시도==@sido')

    fig = make_subplots(specs=[[{"secondary_y": True}]])
    fig.add_trace(go.Scatter(x=data['연도'], y=data['인구수'], mode='lines', name='인구수'), secondary_y=False)
    fig.add_trace(go.Scatter(x=data['연도'], y=data['사용량'], mode='lines', name='전력사용량'), secondary_y=True)

    fig.update_xaxes(range=[2011,2021], tickmode='linear', dtick=1)
    fig.update_yaxes(title_text="인구수", secondary_y=False)
    fig.update_yaxes(title_text="전력사용량", secondary_y=True)

    fig.update_layout(title='인구수 - 전력 사용량 추이')
    fig.show()