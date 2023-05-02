from django.shortcuts import render
from django.http import HttpResponse

### 전력량 지도맵 시각화 사용자 라이브러리
from referenceapp.usage.usage import Usage_map
from referenceapp.usage.usage_data import Data_View

# reference 페이지
def reference(request):
    ### 클래스 생성시키기
    map_view = Usage_map()
    data_view = Data_View()
    ### 지도 생성을 위한 인자값 받기
    year = request.GET.get('year', 'ERROR')
    if year == 'ERROR':
        year = 2016
        
    month = request.GET.get('month', 'ERROR')
    if month == 'ERROR':
        month = 1
        
    ### 특정년도 dataframe 생성 및 가져오기
    area = request.GET.get('area', 'ERROR')
    if area == 'ERROR':
        area = '서울특별시'
    year_area_data = data_view.setYearDataFrame(year, area)
        
    ### 지도 생성을 위한 인자값 넣어서 dataframe 생성
    map_data = map_view.setDataFrame(year, month) 
    
    ### 지도맵 생성 및 가져오기
    map_view.getMap()
    map_html = map_view.map_base()
    
    ### 그래프 생성 및 가져오기
    fig = data_view.initVisualization(year, area)
    
    ### 전력량 데이터프레임 받아오기
    map_data = map_view.getDataFrame().to_html()
    return render(request, 'referenceapp/reference.html', {"map_html" : map_html,
                                                           "map_data" : map_data,
                                                           "year_data" : year,
                                                           "month_data" : month,
                                                           "area_data" : area,
                                                           "fig" : fig})

#######################
##### 지도맵 시각화 ####
#######################
# - 지도맵 사용자 라이브러리 불리들이기
def map_Visualization(request) :
    ### 클래스 생성시키기
    map_view = Usage_map()
    data_view = Data_View()
    ### 지도 생성을 위한 인자값 받기
    year = request.GET.get('year', 'ERROR')
    if year == 'ERROR':
        year = 2016
        
    month = request.GET.get('month', 'ERROR')
    if month == 'ERROR':
        month = 1
        
    ### 특정년도 dataframe 생성 및 가져오기
    area = request.GET.get('area', 'ERROR')
    if area == 'ERROR':
        area = '서울특별시'
    year_area_data = data_view.setYearDataFrame(year, area)
        
    ### 지도 생성을 위한 인자값 넣어서 dataframe 생성
    map_data = map_view.setDataFrame(year, month)    
    ### 지도맵 생성 및 가져오기
    map_view.getMap()
    map_html = map_view.map_base()
    
    ### 그래프 생성 및 가져오기
    fig = data_view.initVisualization(year, area)
    
    ### 전력량 데이터프레임 받아오기
    map_data = map_view.getDataFrame().to_html()

    return render(request,
                  'referenceapp/reference.html',
                  {"map_html" : map_html,
                   "map_data" : map_data,
                   "year_data" : year,
                   "month_data" : month,
                   "area_data" : area,
                   "fig" : fig})
