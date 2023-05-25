import pandas as pd
import json
import folium

class Grdp_map :

    def __init__(self):
        self.initDataFrame()
        self.initJson()

    def initDataFrame(self):
        file_path = "./yearmapapp/grdp/전력량_grdp_마커.csv"
        self.usage_data = pd.read_csv(file_path)
        self.usage_data.drop(columns=['Unnamed: 0'], inplace=True)

    def setDataFrame(self, year_data) :
        year = year_data
        if year is "ERROR":
            year = 2021
        year = int(year)

        self.df_ver = self.usage_data.query('연도 == @year')
        self.df_data = self.df_ver[['시도', '사용량', '지역내총생산', '위도', '경도']]
        self.df_data_test = self.df_data.to_dict(orient='records')

    def initJson(self) :
        jsonfile = open('./yearmapapp/grdp/Sido.json','r',encoding='utf8').read()     
        self.jsondata = json.loads(jsonfile)                             
        self.jsondata_loc = {'type': 'FeatureCollection'}                
        self.jsondata_pick = []

    def getMap(self) :
        for idx in self.jsondata['features']:
            idx['id'] = idx['properties']['CTP_KOR_NM']             
            for i in self.df_data_test:
                if i['시도'] == idx['properties']['CTP_KOR_NM']:    
                    idx['properties']['pop'] = i['지역내총생산']         
            self.jsondata_pick.append(idx)                               
        self.jsondata_loc['features'] = self.jsondata_pick 

    def map_base(self) :
        self.grdp_map = folium.Map(location=[36.0068191, 127.6607805],zoom_start=7) 
        cho = folium.Choropleth(geo_data=self.jsondata_loc,              
                        data=self.df_data,                          
                        columns=['시도', '지역내총생산'],              
                        fill_color="YlGnBu",
                        key_on='feature.id',
                        legend_name='맵').add_to(self.grdp_map)       
        cho.geojson.add_child( 
            folium.features.GeoJsonPopup(['CTP_KOR_NM','pop'],labels=False,style='font-weight : bold')
        )
        for row in self.df_data_test:
            lat = row['위도']
            lon = row['경도']
            folium.CircleMarker(location=[lat, lon],
                                radius=row['사용량'] / 7000000, # 전력량 값을 radius로 사용
                                color='red',
                                fill_color='red',
                                fill_opacity=0.3,
                                popup=(row['시도'], row['사용량']),
                                tooltip=row['시도']).add_to(cho)
        
        return self.grdp_map._repr_html_()

    def getDataFrame(self):
        return self.df_data