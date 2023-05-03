from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

### 전력량 주택가격변동률 시각화 사용자 라이브러리
from residenceapp.residence.residence_map import Residence_map
from residenceapp.residence.residence_graph import Data_View

# Create your views here.
def residence(request) :
    ### 클래스 생성시키기
    data_view2 = Data_View()
    map_view = Residence_map()
    
    ### 그래프 생성을 위한 인자값 받기
    year = request.GET.get('year_data', 'ERROR')
    if year == 'ERROR':
        year = 2021
    year = int(year)
    
    month = request.GET.get('month_data', 'ERROR')
    if month == 'ERROR':
        month = 1
    month = int(year)
       
    ### 그래프 생성 및 가져오기
    data_view = data_view2.setYearDataFrame(year, month)
    fig = data_view2.initVisualization(data_view)
    
    ### 지도 생성을 위한 인자값 넣어서 dataframe 생성
    map_data = map_view.setDataFrame(year, month) 
    
    ### 지도맵 생성 및 가져오기
    map_view.getMap()
    map_html = map_view.map_base()
    
    return render(request, 'residenceapp/residence.html', {"data_view" : data_view,
                                                            "year_data" : year,
                                                            "month_data" : month,
                                                            "area_data" : area,
                                                            "fig" : fig})

