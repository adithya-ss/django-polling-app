from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse

# Create your views here.
from .models import Questions, Choice

# Get questions and display them.
def index(request):
    latest_questions_list = Questions.objects.order_by('-publish_date')[:5]
    context = {'latest_questions_list': latest_questions_list}
    return render(request, 'polls/index.html', context)

# Show specific question and choices
def detail(request, question_id):
    try:
        question = Questions.objects.get(pk=question_id)
    except Questions.DoesNotExist:
        raise Http404("Question does not exist.")
    return render(request, 'polls/detail.html', { 'question': question })

# Get question and display results
def results(request, question_id):
    question = get_object_or_404(Questions, pk=question_id)
    return render(request, 'polls/results.html', { 'question': question })

#Vote for a question choice
def vote(request, question_id):
    question = get_object_or_404(Questions, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
        'question': question,
        'error_message': "Choice not selected."
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
