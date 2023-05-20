from django.shortcuts import render
from . import models
# Create your views here.

def work(request):
    works = models.Works.objects.all().order_by('-date')
    return render(request, 'work\work.html', {'works':works})

def d_work(request, slug):
    work = models.Works.objects.get(slug=slug)
    return render(request, 'work\works.html', {'work':work})