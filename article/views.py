from django.shortcuts import render
from .models import Article
from .forms import ArticleForm
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import JsonResponse


def index(request):
    # articles = Article.objects.all()
    # articles = articles[:3]
    # return render(request, 'article_index.html', {'articles': articles})
    full_articles = Article.objects.all()
    three_articles = full_articles[:3]
    context = {
        'full_articles': full_articles,
        'three_articles': three_articles
    }
    return render(request, 'article_index.html', context)


@login_required(login_url='/admin/login/')
def add_article(request):
    context = {}
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            form = ArticleForm()
    else:
        form = ArticleForm()
    context['form'] = form
    return render(request, 'article_form.html', context)


def detail_article(request, uniq):
    articles = Article.objects.get(judul=uniq)
    return render(request, 'article_detail.html', {'articles': articles})


def load_more(request):
    offset = int(request.POST['offset'])
    limit = 3
    posts = Article.objects.all()[offset:limit+offset]
    totalData = Article.objects.count()
    data = {}
    posts_json = serializers.serialize('json', posts)
    return JsonResponse(data={
        'posts': posts_json,
        'totalResult': totalData
    })
