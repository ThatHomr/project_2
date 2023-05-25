from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

### 전력량 및 요소 그래프 시각화 사용자 라이브러리
from yearmapapp.local.local_graph import Data_View
from yearmapapp.grdp.grdp_graph import Data_grdp_View
from yearmapapp.factory.factory_graph import Data_factory_View
from yearmapapp.medical.medical_graph import Data_medical_View
from yearmapapp.hospital.numbed_graph import Num_bed_View

### grdp 지도
from yearmapapp.local.local_map import Local_map
from yearmapapp.grdp.grdp_map import Grdp_map
from yearmapapp.factory.factory_map import Factory_map
from yearmapapp.medical.medical_map import Medical_map
from yearmapapp.hospital.numbed_map import Num_bed_map


def local(request) :
    ### 클래스 생성시키기
    map_view2 = Local_map()
    data_view2 = Data_View()
    name = "지방세"
    
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
    return render(request, 'yearmapapp/yearmap.html', {"data_view" : data_view,
                                                    "year_data" : year,
                                                    "area_data" : area,
                                                    "map_html" : map_view,
                                                    "fig" : fig,
                                                    "name" : name})

def grdp(request) :
    ### 클래스 생성시키기
    map_view2 = Grdp_map()
    data_view2 = Data_grdp_View()
    name = "지역내생산(grdp)"
    
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
    return render(request, 'yearmapapp/yearmap.html', {"data_view" : data_view,
                                                    "year_data" : year,
                                                    "area_data" : area,
                                                    "map_html" : map_view,
                                                    "fig" : fig,
                                                    "name" : name})
    
def factory(request) :
    ### 클래스 생성시키기
    data_view2 = Data_factory_View()
    map_view = Factory_map()
    name = "공장면적"
    
    ### 그래프 생성을 위한 인자값 받기
    year = request.GET.get('year_data', 'ERROR')
    if year == 'ERROR':
        year = 2021
    year = int(year)
    
    area = request.GET.get('area_data', 'ERROR')
    if area == 'ERROR':
        area = '서울특별시'
       
    ### 그래프 생성 및 가져오기
    data_view = data_view2.setYearDataFrame(area)
    fig = data_view2.initVisualization(data_view)
    
    ### 지도 생성을 위한 인자값 넣어서 dataframe 생성
    map_data = map_view.setDataFrame(year)
    
    ### 지도맵 생성 및 가져오기
    map_view.getMap()
    map_html = map_view.map_base()
    
    return render(request, 'yearmapapp/yearmap.html', {"data_view" : data_view,
                                                        "map_html" : map_html,
                                                        "year_data" : year,
                                                        "area_data" : area,
                                                        "fig" : fig,
                                                        "name" : name})

def medical(request) :
    ### 클래스 생성시키기
    data_view2 = Data_medical_View()
    map_view = Medical_map()
    name = "의료인수"
    
    ### 그래프 생성을 위한 인자값 받기
    year = request.GET.get('year_data', 'ERROR')
    if year == 'ERROR':
        year = 2021
    year = int(year)
    
    area = request.GET.get('area_data', 'ERROR')
    if area == 'ERROR':
        area = '서울특별시'
       
    ### 그래프 생성 및 가져오기
    data_view = data_view2.setYearDataFrame(area)
    fig = data_view2.initVisualization(data_view)
    
    ### 지도 생성을 위한 인자값 넣어서 dataframe 생성
    map_data = map_view.setDataFrame(year)
    
    ### 지도맵 생성 및 가져오기
    map_view.getMap()
    map_html = map_view.map_base()
    
    return render(request, 'yearmapapp/yearmap.html', {"data_view" : data_view,
                                                        "map_html" : map_html,
                                                        "year_data" : year,
                                                        "area_data" : area,
                                                        "fig" : fig,
                                                        "name" : name})


def hospital(request) :
    ### 클래스 생성시키기
    data_view2 = Num_bed_View()
    map_view = Num_bed_map()
    name = "병동수"
    
    ### 그래프 생성을 위한 인자값 받기
    year = request.GET.get('year_data', 'ERROR')
    if year == 'ERROR':
        year = 2021
    year = int(year)
    
    area = request.GET.get('area_data', 'ERROR')
    if area == 'ERROR':
        area = '서울특별시'
       
    ### 그래프 생성 및 가져오기
    data_view = data_view2.setYearDataFrame(area)
    fig = data_view2.initVisualization(data_view)
    
    ### 지도 생성을 위한 인자값 넣어서 dataframe 생성
    map_data = map_view.setDataFrame(year)
    
    ### 지도맵 생성 및 가져오기
    map_view.getMap()
    map_html = map_view.map_base()
    
    return render(request, 'yearmapapp/yearmap.html', {"data_view" : data_view,
                                                        "map_html" : map_html,
                                                        "year_data" : year,
                                                        "area_data" : area,
                                                        "fig" : fig,
                                                        "name" : name})
