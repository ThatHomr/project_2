import pandas as pd
import json
import folium

class Pop_map :

    def __init__(self):
        self.initDataFrame()
        self.initJson()

    def initDataFrame(self):
        file_path = "./2011~2022_인구수(2).csv"
        self.usage_data = pd.read_csv(file_path)
        self.usage_data.drop(columns=['Unnamed: 0'], inplace=True)

    def setDataFrame(self, year_data, month_data) :
        year = year_data
        if year is "ERROR":
            year = 2021
        year = int(year)
        month = month_data
        if month is "ERROR":
            month = 12
        month = int(month)
        self.df_ver = self.usage_data.query('연도 == @year & 월 == @month')
        self.df_data = self.df_ver[['시도', '인구수']]
        self.df_data_test = self.df_data.to_dict(orient='records')

    def initJson(self) :
        jsonfile = open('./Sido.json','r',encoding='utf8').read()     
        self.jsondata = json.loads(jsonfile)                             
        self.jsondata_loc = {'type': 'FeatureCollection'}                
        self.jsondata_pick = []

    def getMap(self) :
        for idx in self.jsondata['features']:
            idx['id'] = idx['properties']['CTP_KOR_NM']             
            for i in self.df_data_test:
                if i['시도'] == idx['properties']['CTP_KOR_NM']:    
                    idx['properties']['pop'] = i['인구수']         
            self.jsondata_pick.append(idx)                               
        self.jsondata_loc['features'] = self.jsondata_pick 

    def map_base(self) :
        self.usage_map = folium.Map(location=[36.0068191, 127.6607805],zoom_start=7) 
        cho = folium.Choropleth(geo_data=self.jsondata_loc,              
                        data=self.df_data,                          
                        columns=['시도', '인구수'],              
                        fill_color="YlGnBu",
                        key_on='feature.id',
                        legend_name='맵').add_to(self.usage_map)       
        cho.geojson.add_child( 
            folium.features.GeoJsonPopup(['CTP_KOR_NM','pop'],labels=False,style='font-weight : bold')
        )
        return self.usage_map._repr_html_()

    def getDataFrame(self):
        return self.usage_data