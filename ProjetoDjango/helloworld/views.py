from ssl import Options
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Question
from django.urls import reverse
from .models import Option
from .utils import get_plot

# Create your views here.
def index(request):
    questions = Question.objects.order_by('question_text')
    context = {'questions': questions}
    return render(request, 'helloworld/index.html',context)

def grafico(request):
    options = Option.objects.all()
    x = [x.option_text for x in options]
    y = [y.votes for y in options]
    chart = get_plot(x, y)
    return render(request, 'helloworld/results.html', {'chart': chart})

def results(request, question_id):
    question = Question(pk=question_id)
    context = {'question': question}
    return render(request, 'helloworld/results.html', context)

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_option = question.option_set.get(pk=request.POST['option'])
    except KeyError:
        return render(request, 'helloworld/vote.html', {
          'question': question,
          'error_message': "Selecione uma opção",
        })
    else:
        selected_option.votes += 1
        selected_option.save()
        return HttpResponseRedirect(reverse('helloworld:results', args=(question_id, )))