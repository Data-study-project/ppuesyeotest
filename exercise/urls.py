from  django.urls import path
from . import views

app_name = "exercise"
urlpatterns = [
    path('get_addr/', views.get_addr, name='get_addr'),
    path('get_locations/', views.get_locations, name='get_locations'),
]