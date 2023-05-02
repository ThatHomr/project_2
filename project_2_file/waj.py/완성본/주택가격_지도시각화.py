def folium(year, month):
    import pandas as pd
    import json
    import folium

    df_1 = pd.read_csv("./지도시각화_전력,주택.csv")
    df_1.drop(columns=['Unnamed: 0'], inplace=True)

    year = year
    month = month

    df_ver = df_1.query('연도 == @year & 월 == @month')
    df_1.query('연도 == @year')

    df_data = df_ver[['시도', '주택가격변동률']]

    df_data_test = df_data.to_dict(orient='records')

    jsonfile = open('Sido.json','r',encoding='utf8').read()     # 시도구분된 지역 json 파일 가져오기
    jsondata = json.loads(jsonfile)                             
    jsondata_loc = {'type': 'FeatureCollection'}                # Sido.json을 복사해서 일부 특성(Key와 Record) 추가
    jsondata_pick = []
    for idx in jsondata['features']:
        idx['id'] = idx['properties']['CTP_KOR_NM']             # Sido.
        for i in df_data_test:
            if i['시도'] == idx['properties']['CTP_KOR_NM']:    # Sido.json의 지역과 일치하면 pop이라는 Key를 새로 만들고
                idx['properties']['pop'] = i['주택가격변동률']         # 해당 지역의 2021.12. 시점의 물가지수를 입력
        jsondata_pick.append(idx)                               # 추가된 값을 jsondata_pick에 저장
    jsondata_loc['features'] = jsondata_pick                    # jsondata_loc의 features 키에 저장

    # 지도 생성, location : 시작위치, zoom_start : 시작 시 확대정도
    map = folium.Map(location=[36.0068191, 127.6607805],zoom_start=7) 
    cho = folium.Choropleth(geo_data=jsondata_loc,              # 색상단계도 생성, geo_data : 참고할 위치정보 데이터
                    data=df_data,                          # data : geo_data와 비교해 맞출 데이터
                    columns=['시도', '주택가격변동률'],              # columns : data에서 사용할 열
                    fill_color="YlGnBu",                      # fill_color : 색 
                    key_on='feature.id',                      # key_on : data와 맞출 geo_data의 데이터
                    legend_name='맵').add_to(map)    # legend_name : 범례 제목 입력       
    cho.geojson.add_child(                                      # 속성 부여
        folium.features.GeoJsonPopup(['CTP_KOR_NM','pop'],labels=False,style='font-weight : bold')
    )   # popup 넣기, geo_data의 properties 키의 값들 중 선택 가능, labels : 열이름 유무, style : 서식
    return map.to_html()

