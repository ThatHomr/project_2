import pandas as pd
import matplotlib.pyplot as plt




# 시각화 함수
def plot(target_year):

    # 데이터 호출
    df_usage_kospi = pd.read_csv('전력사용량,코스피.csv')

    # 타겟 기간 호출
    df_usage_kospi = df_usage_kospi[df_usage_kospi['연도'] == target_year]

    df_usage_kospi['사용량'].to_list()
    df_usage_list = list(df_usage_kospi['사용량'])
    df_usage_kospi['코스피 평균'].to_list()
    df_kospi_list = list(df_usage_kospi['코스피 평균'])
    df_usage_kospi['년월'].to_list()
    date = list(df_usage_kospi['월'])

    # 그래프 데이터 생성
    x = date
    y1 = df_usage_list
    y2 = df_kospi_list

    # 그래프 객체 생성
    fig, ax = plt.subplots()

    ax.set_title('전력 사용량 VS 코스피')

    # 첫 번째 그래프 그리기
    ax.plot(x, y1, color='red', label='전력 사용량')
    ax.set_ylabel('전력 사용량')
    ax.tick_params('y', colors='red')

    # 두 번째 그래프 그리기
    ax2 = ax.twinx()
    ax2.plot(x, y2, color='blue', label='코스피')
    ax2.set_ylabel('코스피')
    ax2.tick_params('y', colors='blue')

    # 범례 표시
    ax.legend(loc='upper left')
    ax2.legend(loc='upper right')

    # 그래프 보여주기
    plt.show()