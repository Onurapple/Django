from django.urls import path
from .views import contacts_page, get_contacts

urlpatterns = [
    path('', contacts_page, name='contacts_page'),
    path('listeli/', get_contacts, name='get_contacts'),
    
]