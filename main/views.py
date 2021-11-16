from django.shortcuts import render

from main.models import Health
from survey.models import Survey

from django.conf import settings

# Create your views here.
def index(request):
    healths = Health.objects.all()
    survey_cnt = Survey.objects.all().count()

    API_KEY_SHARE_KAKAO = getattr(settings, 'API_KEY_SHARE_KAKAO', 'API_KEY_SHARE_KAKAO')

    context = {
        'healths': healths,
        'survey_cnt': survey_cnt,
        'api_Key': API_KEY_SHARE_KAKAO,
    }

    return render(request, 'main/index.html', context)