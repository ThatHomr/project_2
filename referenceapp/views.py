from django.shortcuts import render
from django.http import HttpResponse

### 전력량 지도맵 시각화 사용자 라이브러리
from referenceapp.usage.usage import Usage_map

# 최초 인덱스 페이지
def index(request):
    return render(request, 'mainapp\index.html', {})

# reference 페이지
def reference(request):
    ### 클래스 생성시키기
    map_view = Usage_map()
    ### 지도 생성을 위한 인자값 받기
    year_data = request.GET.get('year', 'ERROR')
    month_data = request.GET.get('month', 'ERROR')
    ### 지도 생성을 위한 인자값 넣어서 dataframe 생성
    map_data = map_view.setDataFrame(year_data, month_data)    
    ### 지도맵 생성 및 가져오기
    map_view.getMap()
    map_html = map_view.map_base()
    ### 전력량 데이터프레임 받아오기
    map_data = map_view.getDataFrame().to_html()
    return render(request, 'referenceapp/reference.html', {"map_html" : map_html,
                                                           "map_data" : map_data})

#######################
##### 지도맵 시각화 ####
#######################
# - 지도맵 사용자 라이브러리 불리들이기
def map_Visualization(request) :
    ### 클래스 생성시키기
    map_view = Usage_map()
    ### 지도 생성을 위한 인자값 받기
    year = request.GET.get('year', 'ERROR')
    month = request.GET.get('month', 'ERROR')
    ### 지도 생성을 위한 인자값 넣어서 dataframe 생성
    map_data = map_view.getDataFrame(year, month)    
    ### 지도맵 생성 및 가져오기
    map_view.getMap()
    map_html = map_view.map_base()
    ### 전력량 데이터프레임 받아오기
    map_data = map_view.getDataFrame().to_html()

    return render(request,
                  'referenceapp/reference.html',
                  {"map_html" : map_html,
                   "map_data" : map_data})
