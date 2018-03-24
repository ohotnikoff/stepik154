from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.core.paginator import Paginator
from django.views.decorators.http import require_GET
from django.core.urlresolvers import reverse
from qa.models import Question, Answer

# Create your views here.
@require_GET
def questions_new(request):
    questions = Question.objects.new()
    limit = 10
    try:
        page = int(request.GET.get('page', 1))
    except ValueError:
        raise Http404
    paginator = Paginator(questions, limit)
    paginator.baseurl = reverse('new')+'?page='
    page = paginator.page(page)
    return render(request, 'questions_new.html', {
        'questions': page.object_list,
        'paginator': paginator,
        'page': page,
    })

@require_GET
def questions_popular(request):
    questions = Question.objects.popular()
    limit = 10
    try:
        page = int(request.GET.get('page', 1))
    except ValueError:
        raise Http404
    paginator = Paginator(questions, limit)
    paginator.baseurl = reverse('popular')+'?page='
    page = paginator.page(page)
    return render(request, 'questions_popular.html', {
        'questions': page.object_list,
        'paginator': paginator,
        'page': page,
    })

@require_GET
def question_details(request, id):
    question = get_object_or_404(Question, id=id)
    try:
        answers = Answer.objects.filter(question=question)
    except Answer.DoesNotExist:
        answers = None
    return render(request, 'question_details.html', {
        'question': question,
        'answers': answers,
    })

def test(request, *args, **kwargs):
    return HttpResponse('OK')