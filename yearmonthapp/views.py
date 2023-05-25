from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

### 전력량 지도맵 시각화 사용자 라이브러리
from yearmonthapp.population_density.population_density_map import Pop_map
from yearmonthapp.population_density.population_density_data import Data_View
from yearmonthapp.population_density.population_density_data_all import Data_all_View
from yearmonthapp.people_num.pop_num_map import Pop_num_map
from yearmonthapp.people_num.pop_graph import Data_num_View
from yearmonthapp.people_num.pop_graph_all import Data_num_all

def people_num(request) :
    ### 클래스 생성시키기
    map_view = Pop_num_map()
    data_view2 = Data_num_View()
    data_view3 = Data_num_all()
    name = "인구수"
    ### 지도 생성을 위한 인자값 받기
    year = request.GET.get('year_data', 'ERROR')
    if year == 'ERROR':
        year = 2021
    year = int(year)
        
    month = request.GET.get('month_data', 'ERROR')
    if month == 'ERROR':
        month = 1
    month = int(month)
        
    ### 특정년도 dataframe 생성 및 가져오기
    area = request.GET.get('area_data', 'ERROR')
    if area == 'ERROR':
        area = '서울특별시'
    data_view = data_view2.setYearDataFrame(year, area)
    data_view1 = data_view3.setYearDataFrame(area)
        
    ### 지도 생성을 위한 인자값 넣어서 dataframe 생성
    map_data = map_view.setDataFrame(year, month) 
    
    ### 지도맵 생성 및 가져오기
    map_view.getMap()
    map_html = map_view.map_base()
    
    ### 그래프 생성 및 가져오기
    fig = data_view2.initVisualization(data_view)
    fig2 = data_view3.initVisualization(data_view1)
    
    return render(request, 'yearmonthapp/yearmonth.html', {"map_html" : map_html,
                                                         "data_view" : data_view,
                                                           "year_data" : year,
                                                           "month_data" : month,
                                                           "area_data" : area,
                                                           "fig" : fig,
                                                           "fig2" : fig2,
                                                           "name" : name})

def people_pop(request):
    ### 클래스 생성시키기
    map_view = Pop_map()
    data_view2 = Data_View()
    data_view3 = Data_all_View()
    name = "인구밀도"
    ### 지도 생성을 위한 인자값 받기
    year = request.GET.get('year_data', 'ERROR')
    if year == 'ERROR':
        year = 2021
    year = int(year)
        
    month = request.GET.get('month_data', 'ERROR')
    if month == 'ERROR':
        month = 1
    month = int(month)
        
    ### 특정년도 dataframe 생성 및 가져오기
    area = request.GET.get('area_data', 'ERROR')
    if area == 'ERROR':
        area = '서울특별시'
    data_view = data_view2.setYearDataFrame(year, area)
    data_view1 = data_view3.setYearDataFrame(area)
        
    ### 지도 생성을 위한 인자값 넣어서 dataframe 생성
    map_data = map_view.setDataFrame(year, month) 
    
    ### 지도맵 생성 및 가져오기
    map_view.getMap()
    map_html = map_view.map_base()
    
    ### 그래프 생성 및 가져오기
    fig = data_view2.initVisualization(data_view)
    fig2 = data_view3.initVisualization(data_view1)
    
    return render(request, 'yearmonthapp/yearmonth.html', {"map_html" : map_html,
                                                         "data_view" : data_view,
                                                           "year_data" : year,
                                                           "month_data" : month,
                                                           "area_data" : area,
                                                           "fig" : fig,
                                                           "fig2" : fig2,
                                                           "name" : name})