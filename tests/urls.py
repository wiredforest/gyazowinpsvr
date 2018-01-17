from django.urls import path, include
from gyazosvr import urls as gyazo_urls

urlpatterns = [
    path('', include(gyazo_urls), name='gyazosvr'),
]
