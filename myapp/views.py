from django.shortcuts import render
from django.http import HttpResponse
from . import models
import time
import datetime
# Create your views here.



def index(request):
    t = time.strftime('%Y-%m-%d', time.localtime(time.time()+300))
    t_array = t.split('-')
    d = datetime.date(int(t_array[0]), int(t_array[1]), int(t_array[2])).isocalendar()
    n = d[1] * 7 - 7 + d[2]
    obj = models.Poem.objects.get(pk=n)
    return render(request,'myapp/index.html',{'time':t,'obj':obj})
