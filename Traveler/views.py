from django.shortcuts import render, redirect, get_object_or_404
from .models import Traveler
from .forms import TravelerForm

def create_traveler(request):
    if request.method == 'POST':
        form = TravelerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_trips')
    else:
        form = TravelerForm()
    has_profile = Traveler.objects.exists()
    return render(request, 'create-traveler.html', {'form': form, 'has_profile': has_profile})

def traveler_details(request):
    has_profile = Traveler.objects.exists()
    traveler = Traveler.objects.first()
    if traveler:
        return render(request, 'details-traveler.html', {'traveler': traveler, 'has_profile': has_profile})
    return redirect('create_traveler')

def edit_traveler(request):
    has_profile = Traveler.objects.exists()
    traveler = get_object_or_404(Traveler)
    if request.method == 'POST':
        form = TravelerForm(request.POST, instance=traveler)
        if form.is_valid():
            form.save()
            return redirect('traveler_details')
    else:
        form = TravelerForm(instance=traveler)
    return render(request, 'edit-traveler.html', {'form': form, 'has_profile': has_profile})

def delete_traveler(request):
    has_profile = Traveler.objects.exists()
    traveler = get_object_or_404(Traveler)
    if request.method == 'POST':
        traveler.delete()
        return redirect('index')
    return render(request, 'delete-traveler.html', {'traveler': traveler, 'has_profile': has_profile})
