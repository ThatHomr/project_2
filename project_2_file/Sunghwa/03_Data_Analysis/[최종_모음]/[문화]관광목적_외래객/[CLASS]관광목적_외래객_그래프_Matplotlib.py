### 라이브러리 불러들이기

import pandas as pd
import matplotlib.pyplot as plt
# 한글폰트
import platform
from matplotlib import font_manager, rc

if platform.system() == 'Windows':  # 현재 운영체제가 Windows인 경우
    # 폰트 파일 경로를 지정
    # 해당 폰트 파일의 이름 호출
    font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf"
                                            ).get_name()
    # 폰트 이름과 크기를 설정
    rc('font', family=font_name, size=8)
    plt.rcParams['axes.unicode_minus'] = False




class Tourist_Matplotlib :

    ### 클래스 생성 시점에 아래 함수들 순서대로 호출 실행(저장까지)
    def __init__(self) :
        self.initTourist_DF()        
        self.initTourist_Visualization()
        self.saveTourist_Fig()

    ### 데이터 데이터프레임으로 읽어들이기
    def initTourist_DF(self) :
        self.df = pd.read_csv("기간_관광객_전력소비량.csv")
        
    ### 데이터 전처리를 마친 csv 파일을 로드했으므로 전처리 함수는 생략
    
    ###  그래프 시각화 함수
    def initTourist_Visualization(self) :
        # 폰트 설정
        plt.rcParams['font.family'] = 'D2Coding'  
        plt.rcParams['font.size'] = 15
        plt.rcParams['axes.unicode_minus']=False
        # 그래프 그리기
        fig, ax1 = plt.subplots(figsize=(15,6),nrows=1,ncols=1)

        color_1 = 'tab:blue'
        ax1.set_title('2010~2021 평균 전력소비량 대비 입국 관광객 수', fontsize=12)
        ax1.set_xlabel('기간')
        ax1.set_ylabel('전력소비량', fontsize=12, color=color_1)
        ax1.plot(self.df.index, self.df.전력소비량 , marker='o', color=color_1,linewidth=3)
        ax1.tick_params(axis='y', labelcolor=color_1)


        ax2 = ax1.twinx() 
        color_2 = 'tab:red'
        ax2.set_ylabel('관광객', fontsize=12, color=color_2)
        ax2.plot(self.df.index, self.df.관광객, marker='o', color=color_2,linewidth=3)
        ax2.tick_params(axis='y', labelcolor=color_2)

        fig.tight_layout()
        plt.show()

    ### 그래프 저장하기
    def saveTourist_Fig(self) :
        self.fig.savefig("./Tourist_Matplotlib.png")