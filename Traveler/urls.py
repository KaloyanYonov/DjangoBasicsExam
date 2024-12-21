from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_traveler, name='create_traveler'),  
    path('details/', views.traveler_details, name='traveler_details'),
    path('edit/', views.edit_traveler, name='edit_traveler'), 
    path('delete/', views.delete_traveler, name='delete_traveler'), 
]
