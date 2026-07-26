"""shorter forms"""
from django import forms
from shorter.models import ShortURL



class ShortURLForm(forms.ModelForm):
    """short url form"""

    class Meta:
        """configuration for this form"""
        model = ShortURL
        fields = ('name', 'original_url',)
        widgets = {
            'name': forms.TextInput(attrs={'class': "form-control"}),
            'original_url': forms.URLInput(attrs={'class': "form-control"}),
        }
