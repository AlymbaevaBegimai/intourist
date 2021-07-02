from django.shortcuts import render
from .models import Place

def places(request):
    places_objects = Place.objects.all() #SELCET * FROM Place
    return render(request, 'places.html', {'places':places_objects})
