from django import forms
from .models import Trip

class TripForm(forms.ModelForm):
    class Meta:
        model = Trip
        fields = ['destination', 'summary', 'start_date', 'duration', 'image_url']
        widgets = {
            'destination': forms.TextInput(attrs={
                'placeholder': 'Enter a short destination note...',
                'class': 'form-control',
            }),
            'summary': forms.Textarea(attrs={
                'placeholder': 'Share your exciting moments...',
                'class': 'form-control',
            }),
            'start_date': forms.DateInput(attrs={
                'type': 'date',
                'class': 'form-control',
            }),
            'duration': forms.NumberInput(attrs={
                'value': 1,
                'class': 'form-control',
            }),
            'image_url': forms.URLInput(attrs={
                'placeholder': 'An optional image URL...',
                'class': 'form-control',
            }),
        }
        help_texts = {
            'duration': '*Duration in days is expected.',
        }
