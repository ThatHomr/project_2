from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

### 전력량 및 요소 그래프 시각화 사용자 라이브러리
from yeargraphapp.kospi.kospi import Data_kospi_View
from yeargraphapp.kospi.kospi_all import Data_kospi_all
from yeargraphapp.price.price import Data_price_View
from yeargraphapp.price.price_all import Data_price_all
from yeargraphapp.employment.employment_graph import Data_View
from yeargraphapp.employment.employment_graph_all import Data_all_View
from yeargraphapp.tourism.tourism import Data_tourism_View
from yeargraphapp.tourism.tourism_all import Data_tourism_all
from yeargraphapp.residence.residence_graph import Data_View
from yeargraphapp.residence.residence_graph_all import Data_all_View

# Create your views here.
def kospi(request) :
    ### 클래스 생성시키기
    data_view2 = Data_kospi_View()
    data_view3 = Data_kospi_all()
    name = "코스피"
    
    ### 그래프 생성을 위한 인자값 받기
    year = request.GET.get('year_data', 'ERROR')
    if year == 'ERROR':
        year = 2021
    year = int(year)
       
    data_view = data_view2.setYearDataFrame(year)
    data_view1 = data_view3.setYearDataFrame()
    
    ### 그래프 생성 및 가져오기
    fig = data_view2.initVisualization(data_view)
    fig2 = data_view3.initVisualization(data_view1)
    
    return render(request, 'yeargraphapp/yeargraph.html', {"data_view" : data_view,
                                                            "year_data" : year,
                                                            "fig" : fig,
                                                            "fig2" : fig2,
                                                            "name" : name})

def price_view(request) :
    ### 클래스 생성시키기
    data_view2 = Data_price_View()
    data_view3 = Data_price_all()
    name = "소비자물가지수"
    
    ### 그래프 생성을 위한 인자값 받기
    year = request.GET.get('year_data', 'ERROR')
    if year == 'ERROR':
        year = 2021
    year = int(year)
        
    data_view = data_view2.setYearDataFrame(year)
    data_all = data_view3.setYearDataFrame()
    
    ### 그래프 생성 및 가져오기
    fig2 = data_view2.initVisualization(data_view)
    fig3 = data_view3.initVisualization(data_all)
    
    return render(request, 'yeargraphapp/yeargraph.html', {"data_view" : data_view,
                                                            "year_data" : year,
                                                            "fig" : fig2,
                                                            "fig3" : fig3,
                                                            "name" : name})
    
def employment(request) :
    ### 클래스 생성시키기
    data_view2 = Data_View()
    data_view3 = Data_all_View()
    name = "고용률"
    
    ### 그래프 생성을 위한 인자값 받기
    year = request.GET.get('year_data', 'ERROR')
    if year == 'ERROR':
        year = 2021
    year = int(year)
    
    # month = request.GET.get('month_data', 'ERROR')
    # if month == 'ERROR':
    #     month = 1
    # month = int(year)
    
    area = request.GET.get('area_data', 'ERROR')
    if area == 'ERROR':
        area = '서울특별시'
       
    ### 그래프 생성 및 가져오기
    data_view = data_view2.setYearDataFrame(year, area)
    data_view1 = data_view3.setYearDataFrame(area)
    fig = data_view2.initVisualization(data_view)
    fig2 = data_view3.initVisualization(data_view1)
    
    return render(request, 'yeargraphapp/yeargraph.html', {"data_view" : data_view,
                                                            "year_data" : year,
                                                            "area_data" : area,
                                                            "fig" : fig,
                                                            "fig2" : fig2,
                                                            "name" : name})

def tourism(request) :
    ### 클래스 생성시키기
    data_view2 = Data_tourism_View()
    data_view3 = Data_tourism_all()
    name = "관광객수"
    
    ### 그래프 생성을 위한 인자값 받기
    year = request.GET.get('year_data', 'ERROR')
    if year == 'ERROR':
        year = 2021
    year = int(year)
       
    data_view = data_view2.setYearDataFrame(year)
    data_view1 = data_view3.setYearDataFrame()
    
    ### 그래프 생성 및 가져오기
    fig = data_view2.initVisualization(data_view)
    fig2 = data_view3.initVisualization(data_view1)
    
    return render(request, 'yeargraphapp/yeargraph.html', {"data_view" : data_view,
                                                            "year_data" : year,
                                                            "fig" : fig,
                                                            "fig2" : fig2,
                                                            "name" : name})

def residence(request) :
    ### 클래스 생성시키기
    data_view2 = Data_View()
    data_view3 = Data_all_View()
    name = "주택가격"
    
    ### 그래프 생성을 위한 인자값 받기
    year = request.GET.get('year_data', 'ERROR')
    if year == 'ERROR':
        year = 2021
    year = int(year)
    
    area = request.GET.get('area_data', 'ERROR')
    if area == 'ERROR':
        area = '서울특별시'
       
    ### 그래프 생성 및 가져오기
    data_view = data_view2.setYearDataFrame(year, area)
    data_view1 = data_view3.setYearDataFrame(area)
    fig = data_view2.initVisualization(data_view)
    fig2 = data_view3.initVisualization(data_view1)
    
    return render(request, 'yeargraphapp/yeargraph.html', {"data_view" : data_view,
                                                            "year_data" : year,
                                                            "area_data" : area,
                                                            "fig" : fig,
                                                            "fig2" : fig2,
                                                            "name" : name})
