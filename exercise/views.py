from django.shortcuts import render
from config.settings import API_KEY_MAP

from exercise.models import Exercise

from django.conf import settings

# Create your views here.
def get_addr(request):
    return render(request, 'exercise/get_addr.html')


def get_locations(request):
    my_filter1 = request.POST['data1']
    my_filter2 = request.POST['data2']
    exercises = Exercise.objects.filter(addr__contains=my_filter1).filter(addr__contains=my_filter2)
    API_KEY_MAP = getattr(settings, 'API_KEY_MAP', 'API_KEY_MAP')
    
    context = {
        'exercises': exercises,
        'apiKey': API_KEY_MAP,
    }
    return render(request, 'exercise/get_locations.html', context)