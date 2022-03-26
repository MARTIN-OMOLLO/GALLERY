from django.shortcuts import render
from django.http  import HttpResponse
from .models import Category, Photos

# Create your views here.
def welcome(request):
    photos = Photos.objects.all()
    return render(request, 'welcome.html',{'photos': photos[::-1],})

