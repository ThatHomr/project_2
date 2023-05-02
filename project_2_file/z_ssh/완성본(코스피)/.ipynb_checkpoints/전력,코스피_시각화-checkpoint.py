def plotly(target_year):

    import plotly.graph_objects as go
    import pandas as pd


    # 데이터 호출
    df_usage_kospi = pd.read_csv('전력사용량,코스피.csv')


    # 타겟 기간 호출
    df_usage_kospi = df_usage_kospi[df_usage_kospi['연도'] == target_year]

    # 첫번째 x축을 기준으로 그래프 생성
    trace1 = go.Scatter(
        x = df_usage_kospi['월'],
        y = df_usage_kospi['사용량'],
        name='전력 사용량'
    )

    # 두번째 x축을 기준으로 그래프 생성
    trace2 = go.Scatter(
        x = df_usage_kospi['월'],
        y = df_usage_kospi['코스피 평균'],
        name='코스피',
        yaxis='y2'
    )

    # 하나의 x축과 두 개의 y축으로 레이아웃 생성
    layout = go.Layout(
        title='전력 사용량 VS 코스피 지수',
        yaxis=dict(
            title='전력 사용량'
        ),
        yaxis2=dict(
            title='코스피 지수',
            overlaying='y',
            side='right'
        )
    )

    # 레이아웃 조합 후 그래프 작성
    fig = go.Figure(data=[trace1, trace2], layout=layout)

    # 그래프 표시
    fig.show()
