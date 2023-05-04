from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

### 전력량 및 요소 그래프 시각화 사용자 라이브러리
from priceapp.kospi.kospi import Data_kospi_View
from priceapp.kospi.kospi_all import Data_kospi_all
from priceapp.price.price import Data_price_View
from priceapp.price.price_all import Data_price_all
from priceapp.grdp.grdp_graph import Data_grdp_View
### grdp 지도
from priceapp.grdp.grdp_map import Grdp_map

# Create your views here.
def kospi(request) :
    ### 클래스 생성시키기
    data_view2 = Data_kospi_View()
    data_view3 = Data_kospi_all()
    
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
    
    return render(request, 'priceapp/kospi.html', {"data_view" : data_view,
                                                    "year_data" : year,
                                                    "fig" : fig,
                                                    "fig2" : fig2})

def price_view(request) :
    ### 클래스 생성시키기
    data_view2 = Data_price_View()
    data_view3 = Data_price_all()
    
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
    
    return render(request, 'priceapp/price.html', {"data_view" : data_view,
                                                    "year_data" : year,
                                                    "fig" : fig2,
                                                    "fig3" : fig3})
    
    
def grdp(request) :
    ### 클래스 생성시키기
    map_view2 = Grdp_map()
    data_view2 = Data_grdp_View()
    
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
    return render(request, 'priceapp/grdp.html', {"data_view" : data_view,
                                                    "year_data" : year,
                                                    "area_data" : area,
                                                    "map_html" : map_view,
                                                    "fig" : fig})
