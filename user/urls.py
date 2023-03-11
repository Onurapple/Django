from django.urls import path
from .views import contacts_create_list, contact_update, contact_delete

urlpatterns = [
    path('', contacts_create_list, name='contacts_create_list'),
    path('update/<int:id>', contact_update, name='contact_update'),
    path('delete/<int:id>', contact_delete, name='contact_delete'),
    # path('listeli/', get_contacts, name='contacts_create_list'),
    
]