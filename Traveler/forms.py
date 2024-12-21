from django import forms
from .models import Traveler

class TravelerForm(forms.ModelForm):
    class Meta:
        model = Traveler
        fields = ['nickname', 'email', 'country', 'about_me']
        widgets = {
            'nickname': forms.TextInput(attrs={
                'placeholder': 'Enter a unique nickname...',
                'class': 'form-control',
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Enter a valid email address...',
                'class': 'form-control',
            }),
            'country': forms.TextInput(attrs={
                'placeholder': 'Enter a country code like <BGR>...',
                'class': 'form-control',
            }),
            'about_me': forms.Textarea(attrs={
                'placeholder': 'Tell us about yourself...',
                'class': 'form-control',
            }),
        }
        help_texts = {
            'nickname': '*Nicknames can contain only letters and digits.',
        }
