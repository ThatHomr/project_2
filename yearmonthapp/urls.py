from django.urls import path
from . import views

urlpatterns = [
    path('', views.people_num),
    ########### [지도 시각화] 처리 ########
    ### http://127.0.0.1:8000/people/people_num/
    path('people_num/', views.people_num),
    ### http://127.0.0.1:8000/people/people_pop/
    path('people_pop/', views.people_pop),
]
