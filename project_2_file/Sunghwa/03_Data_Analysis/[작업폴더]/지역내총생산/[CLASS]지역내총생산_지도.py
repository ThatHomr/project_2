### 데이터프레임을 사용할 수 있는 라이브러리 불러들이기
import pandas as pd

import json

### 지도 시각화 라이브러리 불러들이기
import folium

class GRDP_map :
    
    ### 클래스 생성시 아래 함수 모두 실행시키기
    # - 생성자에서 호출
    def __init__(self) :
        self.initDataFrame()
        self.initJson()
        
    ### 데이터 읽어들이기
    def initDataFrame(self) :
        file_path = "시도_연도_GRDP.csv"
        self.GRDP_data = pd.read_csv(file_path)
        self.GRDP_data.drop(columns=['Unnamed: 0'], inplace=True)
        
    # 연도 받아와서 데이터 프레임 만들기
    def setDataFrame(self, year_data) :
        year = year_data
        if year is "ERROR":
            year = 2021
        year = int(year)
        
        self.df_ver = self.GRDP_data.query('연도 == @year')
        self.df_data = self.df_ver[['시도', '지역내총생산']]
        self.df_data_test = self.df_data.to_dict(orient='records')
        
    # json
    def initJson(self) :
        # 시도구분된 지역 json 파일 가져오기
        jsonfile = open('Sido.json','r',encoding='utf8').read()     
        self.jsondata = json.loads(jsonfile)                             
        # Sido.json을 복사해서 일부 특성(Key와 Record) 추가
        self.jsondata_loc = {'type': 'FeatureCollection'}                
        self.jsondata_pick = []
        
    # 데이터에 대한 지도 맵 생성
    def getMap(self) :
        for idx in self.jsondata['features']:
            # Sido.
            idx['id'] = idx['properties']['CTP_KOR_NM']             
            for i in self.df_data_test:
                # Sido.json의 지역과 일치하면 pop이라는 Key를 새로 만들고
                if i['시도'] == idx['properties']['CTP_KOR_NM']:    
                    # 해당 지역의 GRDP 입력
                    idx['properties']['pop'] = i['지역내총생산']         
            # 추가된 값을 jsondata_pick에 저장
            self.jsondata_pick.append(idx)                               
        # jsondata_loc의 features 키에 저장
        self.jsondata_loc['features'] = self.jsondata_pick                         
        
    ### 지도맵 그리기
    def map_base(self) :
        # 지도 생성, location : 시작위치, zoom_start : 시작 시 확대정도
        self.GRDP_map = folium.Map(location=[36.0068191, 127.6607805],zoom_start=7) 
        # 색상단계도 생성, geo_data : 참고할 위치정보 데이터
        cho = folium.Choropleth(geo_data=self.jsondata_loc,              
                        # data : geo_data와 비교해 맞출 데이터
                        data=self.df_data,                          
                        # columns : data에서 사용할 열
                        columns=['시도', '지역내총생산'],              
                        fill_color="YlGnBu",                      # fill_color : 색 
                        key_on='feature.id',                      # key_on : data와 맞출 geo_data의 데이터
                        legend_name='년도 행정구역별 지역내총생산(GRDP)').add_to(self.GRDP_map)    # legend_name : 범례 제목 입력       
        cho.geojson.add_child(                                      # 속성 부여
            folium.features.GeoJsonPopup(['CTP_KOR_NM','pop'],labels=False,style='font-weight : bold')
        )
        return self.GRDP_map._repr_html_()
    
    ### 데이터프레임 리턴하기
    def getDataFrame(self) :
        return self.GRDP_data