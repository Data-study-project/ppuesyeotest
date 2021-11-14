from django.shortcuts import get_object_or_404, render
from survey.models import Survey
from .models import BMI, Walk, Animal
from django.db.models import Avg
import random

from django.conf import settings

EX_LIST = { 
    '111': [('롤러스케이트', '1'), ('헬스', '2')],
    '110': [('피겨', '3'), ('리듬체조', '4'), ('권투', '5')],
    '101': [('농구', '6'), ('에어로빅', '7')],
    '100': [('하키', '8'), ('합기도', '9'), ('태권도', '10')],
    '011': [('롤러스케이트', '1'), ('자전거', '12'), ('조깅', '13'), ('등산', '14')],
    '010': [('사이클', '15'), ('스케이트보드', '16'), ('양궁', '17')],
    '001': [('축구', '18'), ('농구', '6')],
    '000': [('야구', '11'), ('테니스', '20')]
    }


def get_bmi(h, w):
    return round(w / ((h/100) ** 2), 2)


def get_bmi_avg(user_age, user_sex):
    b_avg = BMI.objects.filter(age=user_age, sex=user_sex).aggregate(Avg('body_mass'))
    return round(b_avg['body_mass__avg'], 2)



def get_walkcnt_rank(wc, user_age, user_sex):
    others_walkcnt = Walk.objects.filter(age=user_age, sex=user_sex).order_by('-walk_cnt')
    rank = 1
    for other in others_walkcnt:
        if other.walk_cnt < wc:
            break
        rank += 1
    return rank, others_walkcnt.count() + 1



def get_walkcnt_avg(user_age, user_sex):
    wc_avg = Walk.objects.filter(age=user_age, sex=user_sex).aggregate(Avg('walk_cnt'))
    return round(wc_avg['walk_cnt__avg'], 2)



def exercise_recommend(user_indoor, user_alone, user_light):
    tmp = ''
    tmp += str(user_indoor) +str(user_alone) + str(user_light)
    return random.choice(EX_LIST[tmp])


def get_animal_id(wc_percent):
    if wc_percent >= 80:
        return '5'
    elif wc_percent >= 60:
        return '4'
    elif wc_percent >= 40:
        return '3'
    elif wc_percent >= 20:
        return '2'
    else:
        return '1'


def get_result(request, survey_pk):

    survey = get_object_or_404(Survey, pk=survey_pk)
    exercise, exercise_id = exercise_recommend(survey.indoor, survey.alone, survey.light)

    user_bmi = get_bmi(survey.height, survey.weight)

    bmi_avg = get_bmi_avg(survey.age, survey.sex)


    user_wc_rank, wc_data_cnt = get_walkcnt_rank(survey.walk_cnt, survey.age, survey.sex)
    user_wc_rate = round(user_wc_rank / wc_data_cnt * 100, 2)
    walkcnt_avg = get_walkcnt_avg(survey.age, survey.sex)

    bmi_gap = round(abs(user_bmi - bmi_avg), 2)

    animal_id = get_animal_id(user_wc_rate)
    animal = Animal.objects.get(animal_num=animal_id)


    API_SHARE_KAKAO = getattr(settings, 'API_KEY_SHARE_KAKAO', 'API_KEY_SHARE_KAKAO')

    context = {
        'survey': survey,

        'animal_id': animal_id,
        'animal': animal,

        'user_bmi': user_bmi,
        'bmi_avg': bmi_avg,
        'bmi_gap': bmi_gap,
        'user_wc_rate': user_wc_rate,
        'walkcnt_avg': walkcnt_avg,

        'exercise':exercise,
        'exercise_id': exercise_id,
        
        'apiKey': API_SHARE_KAKAO,
    }
    return render(request, 'result/result.html', context)


def copyright(request):
    return render(request, 'result/copyright.html')