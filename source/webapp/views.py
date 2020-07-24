from django.shortcuts import render
from webapp.models import Article, STATUS_CHOICES
from django.http import HttpResponseNotAllowed


def index_view(request):
    data = Article.objects.all()
    return render(request, 'index.html', context={
        'articles': data
    })


def tasks_new_view(request):
    data = Article.objects.filter(status='new')
    return render(request, 'new.html', context={
        'articles': data
    })


def tasks_moderated_view(request):
    data = Article.objects.filter(status='moderated')
    return render(request, 'moderated.html', context={
        'articles': data
    })


def tasks_rejected_view(request):
    data = Article.objects.filter(status='rejected')
    return render(request, 'rejected.html', context={
        'articles': data
    })


def article_create_view(request):
    if request.method == "GET":
        return render(request, 'article_create.html', context={
            'status_choices': STATUS_CHOICES
        })
    elif request.method == 'POST':
        title = request.POST.get('title')
        text = request.POST.get('text')
        author = request.POST.get('author')
        status = request.POST.get('status')
        article = Article.objects.create(title=title, text=text, author=author, status=status)
        context = {'article': article}
        return render(request, 'article_view.html', context)
    else:
        return HttpResponseNotAllowed(permitted_methods=['GET', 'POST'])

