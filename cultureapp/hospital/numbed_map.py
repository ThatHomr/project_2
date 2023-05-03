import pandas as pd
import json
import folium

class Num_bed_map :

    def __init__(self):
        self.initDataFrame()
        self.initJson()

    def initDataFrame(self):
        file_path = "./cultureapp/hospital/병상수_마커.csv"
        self.data = pd.read_csv(file_path)
        self.data.drop(columns=['Unnamed: 0'], inplace=True)

    def setDataFrame(self, year_data) :
        year = year_data
        if year is "ERROR":
            year = 2021
        year = int(year)

        self.df_ver = self.data.query('연도 == @year')
        self.df_data = self.df_ver[['시도', '병상수', '사용량', '위도', '경도']]
        self.df_data_test = self.df_data.to_dict(orient='records')

    def initJson(self) :
        jsonfile = open('./cultureapp/hospital/Sido.json','r',encoding='utf8').read()     
        self.jsondata = json.loads(jsonfile)                             
        self.jsondata_loc = {'type': 'FeatureCollection'}                
        self.jsondata_pick = []

    def getMap(self) :
        for idx in self.jsondata['features']:
            idx['id'] = idx['properties']['CTP_KOR_NM']             
            for i in self.df_data_test:
                if i['시도'] == idx['properties']['CTP_KOR_NM']:    
                    idx['properties']['num'] = i['병상수']         
            self.jsondata_pick.append(idx)                               
        self.jsondata_loc['features'] = self.jsondata_pick 

    def map_base(self) :
        self.numbed_map = folium.Map(location=[36.0068191, 127.6607805],zoom_start=7) 
        cho = folium.Choropleth(geo_data=self.jsondata_loc,              
                                data=self.df_data,                          
                                columns=['시도', '병상수'],              
                                fill_color="YlGnBu",
                                key_on='feature.id',
                                legend_name='맵').add_to(self.numbed_map)

        cho.geojson.add_child( 
            folium.features.GeoJsonPopup(['CTP_KOR_NM','num'],labels=False,style='font-weight : bold'))
        for row in self.df_data_test:
            lat = row['위도']
            lon = row['경도']
            folium.CircleMarker(location=[lat, lon],
                                radius=row['사용량'] / 5000000,
                                color='red',
                                fill_color='red',
                                fill_opacity=0.7,
                                tooltip=row['시도']).add_to(cho)

        return self.numbed_map._repr_html_()

    def getDataFrame(self):
        return self.df_data  