from django.shortcuts import render
from . import models
import time
import datetime
from myapp.models import Article
from django.http import Http404



def index(request):
    t = time.strftime('%Y-%m-%d', time.localtime(time.time()+300))
    t_array = t.split('-')
    d = datetime.date(int(t_array[0]), int(t_array[1]), int(t_array[2])).isocalendar()
    n = d[1] * 7 - 7 + d[2] -59
    obj = models.Poem.objects.get(pk=n)
    return render(request,'myapp/index.html',{'time':t,'obj':obj})


def home(request):
    post_list = Article.objects.all() 
    return render(request, 'myapp/home.html', {'post_list': post_list})


def Detail(request, id):
    try:
        post = Article.objects.get(id=str(id))
    except Article.DoesNotExist:
        raise Http404
    return render(request, 'myapp/post.html', {'post': post})
