from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('index/', views.index),
    ### http://127.0.0.1:8000/main/price/
    path('price/', views.price),

]
