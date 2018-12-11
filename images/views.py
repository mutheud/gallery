from django.shortcuts import render
from .models import Image,Location,Category
#................
# Create your views here.
def welcome(request):
    return render(request, 'welcome.html')

def filter_by_location(request,location):
    '''
    Filters the database and displays images according to location_id
    '''
    location = Location.objects.get(name = location)
    images = Image.filter_by_location(location.id)
    return render(request, 'location.html', {"images": images})