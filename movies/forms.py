from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['genres']
        widgets = {
            'genres':forms.CheckboxSelectMultiple(attrs={
                'class':'list-unstyled'
            })
        }