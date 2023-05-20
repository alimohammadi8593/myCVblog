from django.shortcuts import render
from . import models

# Create your views here.
def about(request):
    image = models.Image.objects.all()
    return render(request, 'about/about.html', {'image':image})