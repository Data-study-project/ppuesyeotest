from  django.urls import path
from . import views

app_name = "result"
urlpatterns = [
    path('<int:survey_pk>', views.get_result, name='get_result'),
    path('copyright/', views.copyright, name="copyright"),
]