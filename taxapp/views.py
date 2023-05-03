from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

### 전력량 및 요소 그래프 시각화 사용자 라이브러리
from taxapp.local.local_graph import Data_View
### grdp 지도
from taxapp.local.local_map import Local_map


def local(request) :
    ### 클래스 생성시키기
    map_view2 = Local_map()
    data_view2 = Data_View()
    
    ### 맵 생성을 위한 인자값 받기
    year = request.GET.get('year_data', 'ERROR')
    if year == 'ERROR':
        year = 2021
    year = int(year)
    
    area = request.GET.get('area_data', 'ERROR')
    if area == 'ERROR':
        area = '서울특별시'
    
    ### 맵 데이터 만들고 받기
    map_view2.setDataFrame(year)
    map_view2.getMap()
    map_view = map_view2.map_base()
    
    ### 그래프 데이터 만들고 받기
    data_view = data_view2.setYearDataFrame(area)
    fig = data_view2.initVisualization(data_view)
    return render(request, 'taxapp/local.html', {"data_view" : data_view,
                                                    "year_data" : year,
                                                    "area_data" : area,
                                                    "map_html" : map_view,
                                                    "fig" : fig})
