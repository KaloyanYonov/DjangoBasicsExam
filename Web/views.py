from django.shortcuts import render
from Traveler.models import Traveler

def index(request):
    has_profile = Traveler.objects.exists()
    return render(request, 'index.html', {'has_profile': has_profile})
