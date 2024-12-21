from django.shortcuts import render, redirect, get_object_or_404
from .models import Trip
from .forms import TripForm
from Traveler.models import Traveler

def all_trips(request):
    has_profile = Traveler.objects.exists()
    trips = Trip.objects.all().order_by('-start_date')
    return render(request, 'all-trips.html', {'trips': trips, 'has_profile': has_profile})

def create_trip(request):
    has_profile = Traveler.objects.exists()
    if not has_profile:
        return redirect('create_traveler')
    traveler = Traveler.objects.first()
    if request.method == 'POST':
        form = TripForm(request.POST)
        if form.is_valid():
            trip = form.save(commit=False)
            trip.traveler = traveler
            trip.save()
            return redirect('all_trips')
    else:
        form = TripForm()
    return render(request, 'create-trip.html', {'form': form, 'has_profile': has_profile})

def trip_details(request, trip_pk):
    has_profile = Traveler.objects.exists()
    trip = get_object_or_404(Trip, pk=trip_pk)
    return render(request, 'details-trip.html', {'trip': trip, 'has_profile': has_profile})

def edit_trip(request, trip_pk):
    has_profile = Traveler.objects.exists()
    trip = get_object_or_404(Trip, pk=trip_pk)
    if request.method == 'POST':
        form = TripForm(request.POST, instance=trip)
        if form.is_valid():
            form.save()
            return redirect('all_trips')
    else:
        form = TripForm(instance=trip)
    return render(request, 'edit-trip.html', {'form': form, 'has_profile': has_profile})

def delete_trip(request, trip_pk):
    has_profile = Traveler.objects.exists()
    trip = get_object_or_404(Trip, pk=trip_pk)
    
    if request.method == 'POST':
        trip.delete()
        return redirect('all_trips')
    
    form = TripForm(instance=trip)
    for field in form.fields.values():
        field.disabled = True
    
    return render(request, 'delete-trip.html', {'form': form , 'has_profile' : has_profile})

