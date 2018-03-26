# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.paginator import Paginator
from django.views.decorators.http import require_GET
from django.core.urlresolvers import reverse
from django.contrib import auth
from qa.models import Question, Answer
from qa.forms import AskForm, AnswerForm, LoginForm, SignupForm

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
        'user': request.user,
        'session': request.session,
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

def question_details(request, id):
    question = get_object_or_404(Question, id=id)
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            form.save()
            url = question.get_url()
            return HttpResponseRedirect(url)
    else:
        form = AnswerForm()

    try:
        answers = Answer.objects.filter(question=question)
    except Answer.DoesNotExist:
        answers = None
    return render(request, 'question_details.html', {
        'question': question,
        'answers': answers,
        'form': form,
    })

def ask_form(request):
    if request.method == "POST":
        form = AskForm(request.POST)
        if form.is_valid():
            question = form.save()
            url = question.get_url()
            return HttpResponseRedirect(url)
    else:
        form = AskForm()
    return render(request, 'ask_form.html', {
        'form': form,
    })

def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data["username"]
            password = form.raw_password
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    auth.login(request, user)
            return HttpResponseRedirect(reverse('new'))
    else:
        form = SignupForm()
    return render(request, 'signup.html', {
        'form': form,
        'user': request.user,
        'session': request.session,
    })

def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = auth.authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    auth.login(request, user)
            return HttpResponseRedirect(reverse('new'))
    else:
        form = LoginForm()
    return render(request, 'login.html', {
        'form': form,
        'user': request.user,
        'session': request.session,
    })

def test(request, *args, **kwargs):
    return HttpResponse('OK')
