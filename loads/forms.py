from django import forms
from .models import Loads

class LoadCreateForm(forms.ModelForm):
    class Meta:
        model = Loads
        fields = '__all__'
        #fields = ['first_name', 'last_name']
        # labels = {'last_name': ' SurName', 'first_name': 'Name'}