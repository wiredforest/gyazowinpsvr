from django.urls import path, re_path
from . import views

app_name = 'gyazosvr'

urlpatterns = [
    re_path(r'^$', views.GyazoSvrIndexView.as_view(), name='index'),
]
