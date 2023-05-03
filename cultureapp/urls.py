from django.urls import path
from . import views

urlpatterns = [
    ########### [그래프 시각화] 처리 ########
    ### http://127.0.0.1:8000/culture/tourism/
    path('tourism/', views.tourism),
    ### http://127.0.0.1:8000/culture/medical/
    path('medical/', views.medical),
    ### http://127.0.0.1:8000/culture/hospital/
    path('hospital/', views.hospital),

]
