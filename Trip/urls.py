from django.urls import path
from . import views

urlpatterns = [
    path('all-trips/', views.all_trips, name='all_trips'),  
    path('create/', views.create_trip, name='create_trip'), 
    path('<int:trip_pk>/details/', views.trip_details, name='trip_details'),  
    path('<int:trip_pk>/edit/', views.edit_trip, name='edit_trip'), 
    path('<int:trip_pk>/delete/', views.delete_trip, name='delete_trip'),
]
