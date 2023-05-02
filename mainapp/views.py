from django.shortcuts import render
from django.http import HttpResponse


# 최초 인덱스 페이지
def index(request):
    return render(request, 'mainapp\index.html', {})

# main 페이지
def main(request):
    return render(request, 'mainapp\index.html', {})

# price 페이지
def price(request):
    ### 클래스 생성시키기
    map_view = Usage_map()
    ### 지도 생성을 위한 인자값 받기
    year = request.GET.get('year_data', 'ERROR')
    if year == 'ERROR':
        year = '2016'
        
    month = request.GET.get('month_data', 'ERROR')
    if month == 'ERROR':
        month = '01'
        
    ### 지도 생성을 위한 인자값 넣어서 dataframe 생성
    map_data = map_view.setDataFrame(year, month)    
    
    ### 지도맵 생성 및 가져오기
    map_view.getMap()
    map_html = map_view.map_base()
    
    ### 전력량 데이터프레임 받아오기
    map_data = map_view.getDataFrame().to_html()
    return render(request, 'referenceapp/reference.html', {"map_html" : map_html,
                                                           "map_data" : map_data,
                                                           "year_data" : year,
                                                           "month_data" : month})
