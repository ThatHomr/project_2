from django.urls import path
from . import views

urlpatterns = [
    ########### [그래프 시각화] 처리 ########
    ### http://127.0.0.1:8000/residence/
    path('', views.residence),
    # ### http://127.0.0.1:8000/price/kospi/
    # path('kospi/', views.kospi),
    # ### http://127.0.0.1:8000/price/grdp/
    # path('grdp/', views.grdp),
]
