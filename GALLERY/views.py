from django.shortcuts import render
from django.http  import HttpResponse
from .models import category, Photos

# Create your views here.
def welcome(request):
    photos = Photos.objects.all()
    return render(request, 'welcome.html',{'photos': photos[::-1],})

def details(request):
    photos = Photos.objects.all()
    return render(request, 'all-gallery/details.html',{'photos': photos})


def search_results(request):

    if 'category_name' in request.GET and request.GET["category_name"]:
        search_term = request.GET.get("category_name")
    
        searched_category_name = category.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'all-gallery/search.html',{"message":message,"category_name": searched_category_name})

    else:
        message = "You haven't searched for any term"
        return render(request, 'all-gallery/search.html',{"message":message})