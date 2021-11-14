from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from .models import Survey
from .forms import SurveyForm



@require_http_methods(['GET', 'POST'])
def question(request):
    if request.method == 'POST':
        form = SurveyForm(request.POST)
        if form.is_valid():
            survey = form.save()
            return redirect('result:get_result', survey.pk)
    else:
        form = SurveyForm()
    context  = {
        'form': form,
    }
    return render(request, 'survey/question.html', context)