from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

### 전력량 지도맵 시각화 사용자 라이브러리
from peopleapp.population_density.population_density_map import Pop_map
from peopleapp.population_density.population_density_data import Data_View

def people_num(request) :
    return render(request, 'peopleapp/people_num.html')

def people_pop(request):
    ### 클래스 생성시키기
    map_view = Pop_map()
    data_view2 = Data_View()
    ### 지도 생성을 위한 인자값 받기
    year = request.GET.get('year_data', 'ERROR')
    if year == 'ERROR':
        year = 2021
        
    month = request.GET.get('month_data', 'ERROR')
    if month == 'ERROR':
        month = 1
        
    ### 특정년도 dataframe 생성 및 가져오기
    area = request.GET.get('area_data', 'ERROR')
    if area == 'ERROR':
        area = '서울특별시'
    data_view = data_view2.setYearDataFrame(year, area)
        
    ### 지도 생성을 위한 인자값 넣어서 dataframe 생성
    map_data = map_view.setDataFrame(year, month) 
    
    ### 지도맵 생성 및 가져오기
    map_view.getMap()
    map_html = map_view.map_base()
    
    ### 그래프 생성 및 가져오기
    fig = data_view2.initVisualization(year, area)
    
    return render(request, 'peopleapp/people_pop.html', {"map_html" : map_html,
                                                         "data_view" : data_view,
                                                           "year_data" : year,
                                                           "month_data" : month,
                                                           "area_data" : area,
                                                           "fig" : fig})