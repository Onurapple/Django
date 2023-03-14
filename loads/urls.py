from django.urls import path
from .views import LoadsHomeView, LoadsListView, LoadDetailView, LoadCreateView, LoadUpdateView, LoadDeleteView

urlpatterns = [
    path('', LoadsHomeView.as_view(), name='load_home'),
    path('list/', LoadsListView.as_view(), name='load_list'),
    path('list/add/', LoadCreateView.as_view(), name='load_add'),
    path('list/update/<int:id>/', LoadUpdateView.as_view(), name='load_update'),
    path('list/delete/<int:id>/', LoadDeleteView.as_view(), name='load_delete'),
    path('list/detail/<int:id>/', LoadDetailView.as_view(), name='load_detail')
    
]