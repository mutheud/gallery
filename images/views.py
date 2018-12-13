from django.shortcuts import render
from .models import Image,Location,Category
#................
# Create your views here.
def welcome(request):
    images = Image.objects.all()
    return render(request, 'welcome.html', {"images": images})

def filter_by_location(request,location):
    '''
    Filters the database and displays images according to location_id
    '''
    location = Location.objects.get(name = location)
    images = Image.filter_by_location(location.id)
    return render(request, 'location.html', {"images": images})

def filter_by_category(request, category):
    category = Category.objects.get(name = category)
    images = Image.filter_by_category(category.id)
    return render(request, 'category.html',{"images":images})

def search_image(request):
  
    if 'image' in request.GET and request.GET["image"]:
        category = request.GET.get("image")
        searched_images = Image.search_image(category)
        message = f"{category}"

        return render(request, 'search.html',{"message":message,"images": searched_images})

    else:
        message = ".You haven't searched for any category"
        return render(request, 'search.html',{"message":message})
