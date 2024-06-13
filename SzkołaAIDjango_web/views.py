from django.shortcuts import render
from django.http import HttpResponse
from SzkołaAIDjango_web.models import Article
from django.core import serializers


# Create your views here.
def index(request):
    return HttpResponse("Hello, world!!!!")


def indexArticle(request):
    title = "Lista"
    articles = Article.objects.all()
    return render(request, "articles.html", {
        "title": title,
        "articles": articles
    })


def indexArticleJson(request):
    articles = Article.objects.all()
    data = serializers.serialize('json', articles)
    return HttpResponse(data, content_type="application/json")
