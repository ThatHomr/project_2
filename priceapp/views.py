from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

### 전력량 코스피 시각화 사용자 라이브러리
from priceapp.kospi.kospi import Data_kospi_View
from priceapp.price.price import Data_price_View
### grdp 지도
from priceapp.grdp.grdp import Grdp_map

# Create your views here.
def kospi(request) :
    ### 클래스 생성시키기
    data_view2 = Data_kospi_View()
    
    ### 그래프 생성을 위한 인자값 받기
    year = request.GET.get('year_data', 'ERROR')
    if year == 'ERROR':
        year = 2021
    year = int(year)
       
    data_view = data_view2.setYearDataFrame(year)
    
    ### 그래프 생성 및 가져오기
    fig = data_view2.initVisualization(data_view)
    
    return render(request, 'priceapp/kospi.html', {"data_view" : data_view,
                                                    "year_data" : year,
                                                    "fig" : fig})

def price_view(request) :
    ### 클래스 생성시키기
    data_view2 = Data_price_View()
    
    ### 그래프 생성을 위한 인자값 받기
    year = request.GET.get('year_data', 'ERROR')
    if year == 'ERROR':
        year = 2021
    year = int(year)
        
    data_view = data_view2.setYearDataFrame(year)
    
    ### 그래프 생성 및 가져오기
    fig2 = data_view2.initVisualization(data_view)
    
    return render(request, 'priceapp/price.html', {"data_view" : data_view,
                                                    "year_data" : year,
                                                    "fig" : fig2})
    
    
def grdp(request) :
    ### 클래스 생성시키기
    map_view2 = Grdp_map()
    
    ### 맵 생성을 위한 인자값 받기
    year = request.GET.get('year_data', 'ERROR')
    if year == 'ERROR':
        year = 2021
    year = int(year)
    
    ### 맵 데이터 만들고 받기
    map_view2.setDataFrame(year)
    map_view2.getMap()
    map_view = map_view2.map_base()
    
    return render(request, 'priceapp/price.html', {"data_view" : data_view,
                                                    "year_data" : year,
                                                    "map_view" : map_view})
