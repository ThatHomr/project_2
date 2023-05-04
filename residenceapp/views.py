from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

### 전력량 주택가격변동률 시각화 사용자 라이브러리
from residenceapp.residence.residence_graph import Data_View
from residenceapp.residence.residence_graph_all import Data_all_View

# Create your views here.
def residence(request) :
    ### 클래스 생성시키기
    data_view2 = Data_View()
    data_view3 = Data_all_View()
    
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
    
    return render(request, 'residenceapp/residence.html', {"data_view" : data_view,
                                                            "year_data" : year,
                                                            "area_data" : area,
                                                            "fig" : fig,
                                                            "fig2" : fig2})

