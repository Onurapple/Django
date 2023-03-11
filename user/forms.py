from django import forms
from .models import Contacts

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contacts
        fields = '__all__'
        #fields = ['first_name', 'last_name']
        labels = {'last_name': ' SurName', 'first_name': 'Name'}
