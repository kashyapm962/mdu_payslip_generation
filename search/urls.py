from django.conf.urls import url
from . import views
app_name = 'search'

urlpatterns = [
    url(r'^$', views.index, name ='index'),
    url(r'^result/$' , views.result , name='result'),
    url(r'^upload/$' , views.upload , name='upload'),    
    url(r'^process/$' , views.process , name='process'),    
]


