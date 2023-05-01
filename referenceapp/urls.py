from django.urls import path
from . import views

urlpatterns = [
    path('', views.reference),
    ########### [지도 시각화] 처리 ########
    ### http://127.0.0.1:8000/nonmodel/map_view/
    path('map_view/', views.map_Visualization),

]
