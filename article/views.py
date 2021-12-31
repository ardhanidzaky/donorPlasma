from django.http import response
from django.http.response import HttpResponse
from django.shortcuts import render
from .models import Article
from .forms import ArticleForm
from django.contrib.auth.decorators import login_required
from django.core import serializers
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict
import json


def index(request):
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


@csrf_exempt
def post_artikel(request):
    data = json.loads(request.body)
    form = ArticleForm(data)
    form.save()
    response = HttpResponse('success')
    response.status_code = 200
    return response


@csrf_exempt
def get_artikel(request):
    raw = serializers.serialize('python', Article.objects.all())
    data = [val['fields'] for val in raw]
    out = json.dumps(data)
    return HttpResponse(out, content_type="application/json")
