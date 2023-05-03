from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

### 전력량 및 요소 그래프 시각화 사용자 라이브러리
from cultureapp.tourism.tourism import Data_tourism_View

# Create your views here.
def tourism(request) :
    ### 클래스 생성시키기
    data_view2 = Data_tourism_View()
    
    ### 그래프 생성을 위한 인자값 받기
    year = request.GET.get('year_data', 'ERROR')
    if year == 'ERROR':
        year = 2021
    year = int(year)
       
    data_view = data_view2.setYearDataFrame(year)
    
    ### 그래프 생성 및 가져오기
    fig = data_view2.initVisualization(data_view)
    
    return render(request, 'cultureapp/tourism.html', {"data_view" : data_view,
                                                        "year_data" : year,
                                                        "fig" : fig})
