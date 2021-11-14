from  django.urls import path
from . import views

app_name = "survey"
urlpatterns = [
    path('', views.question, name='question'),
]