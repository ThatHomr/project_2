from django.urls import path
from . import views

urlpatterns = [
    ########### [그래프 시각화] 처리 ########
    ### http://127.0.0.1:8000/yearmap/local/
    path('local/', views.local),
    ### http://127.0.0.1:8000/yearmap/grdp/
    path('grdp/', views.grdp),
    ### http://127.0.0.1:8000/yearmap/factory/
    path('factory/', views.factory),
    ### http://127.0.0.1:8000/culture/medical/
    path('medical/', views.medical),
    ### http://127.0.0.1:8000/culture/hospital/
    path('hospital/', views.hospital),
]
