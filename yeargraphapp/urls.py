from django.urls import path
from . import views

urlpatterns = [
    ########### [그래프 시각화] 처리 ########
    ### http://127.0.0.1:8000/yeargraph/price_view/
    path('price_view/', views.price_view),
    ### http://127.0.0.1:8000/yeargraph/kospi/
    path('kospi/', views.kospi),
    ### http://127.0.0.1:8000/yeargraph/employment/
    path('employment/', views.employment),
    ### http://127.0.0.1:8000/yeargraph/tourism/
    path('tourism/', views.tourism),
    ### http://127.0.0.1:8000/yeargraph/residence_view/
    path('residence_view/', views.residence),
]
