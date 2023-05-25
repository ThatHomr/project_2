from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # http://127.0.0.1:8000/
    path('', include('mainapp.urls')),
    # http://127.0.0.1:8000/index/
    path('index/', include('mainapp.urls')),
    # http://127.0.0.1:8000/main/
    path('main/', include('mainapp.urls')),
    # http://127.0.0.1:8000/yearmonth/
    path('yearmonth/', include('yearmonthapp.urls')),
    # http://127.0.0.1:8000/yearmonth/
    path('yearmap/', include('yearmapapp.urls')),
    # http://127.0.0.1:8000/yearmonth/
    path('yeargraph/', include('yeargraphapp.urls')),
    # http://127.0.0.1:8000/admin/
    path('admin/', admin.site.urls),
]
