from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # http://127.0.0.1:8000/
    path('', include('mainapp.urls')),
    # http://127.0.0.1:8000/index/
    path('index/', include('mainapp.urls')),
    # http://127.0.0.1:8000/main/
    path('main/', include('mainapp.urls')),
    # http://127.0.0.1:8000/reference/
    path('reference/', include('referenceapp.urls')),
    # http://127.0.0.1:8000/people/
    path('people/', include('peopleapp.urls')),
    # http://127.0.0.1:8000/price/
    path('price/', include('priceapp.urls')),
    # http://127.0.0.1:8000/residence/
    path('residence/', include('residenceapp.urls')),
    # http://127.0.0.1:8000/industry/
    path('industry/', include('industryapp.urls')),
    # http://127.0.0.1:8000/culture/
    path('culture/', include('cultureapp.urls')),
    # http://127.0.0.1:8000/tax/
    path('tax/', include('taxapp.urls')),
    # http://127.0.0.1:8000/admin/
    path('admin/', admin.site.urls),
]
