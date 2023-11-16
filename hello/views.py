from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from django.views import generic
from .models import Article

class IndexView(generic.ListView):
    model = Article
    template_name = 'hello/index.html'

def index(request):

    articles = Article.objects.filter(content = 'ちゃお')

    context = {
        'articles': articles,
    }

    return render(request,'hello/index.html', context)