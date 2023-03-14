from django.views.generic import TemplateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import LoadCreateForm
from .models import Loads
from django.urls import reverse_lazy
from django.shortcuts import render, redirect

class LoadsHomeView(TemplateView):
    template_name = "loads/loads.html"
    
    
class LoadsListView(ListView):
    model = Loads
    template_name = "loads/loads_list.html"
    context_object_name = "loads"
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['loads'] = Loads.objects.all()
        #override ederek bu context i ekledik içine.
        return context


class LoadDetailView(DetailView):
    model = Loads
    pk_url_kwarg = "id"
    template_name = "loads/load_detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['load'] = Loads.objects.get(id=self.object.id)
        #override ederek bu context i ekledik içine.
        return context
    
class LoadCreateView(CreateView):
    model = Loads
    form_class = LoadCreateForm
    template_name = "loads/load_add.html"
    success_url = reverse_lazy("load_add")

    def __init__(self):
        self.object = None

    def form_valid(self,form):
        self.object = form.save()
        self.object.save()
        return super(LoadCreateView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['loads'] = Loads.objects.all()
        #override ederek bu context i ekledik içine.
        return context
    
    
class LoadUpdateView(UpdateView):
    model = Loads
    form_class = LoadCreateForm
    template_name = "loads/load_update.html"
    success_url = reverse_lazy("load_add")
    pk_url_kwarg = "id"

    # def get_form(self, *args, **kwargs):
    #     updateform = super(LoadUpdateView, self).get_form(*args, **kwargs)
    #     return updateform
    # 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['loads'] = Loads.objects.all()
        #override ederek bu context i ekledik içine.
        return context
    
    
class LoadDeleteView(DeleteView):
    model = Loads
    template_name = "loads/load_delete.html"
    success_url = reverse_lazy("load_delete")
    pk_url_kwarg = "id"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['load'] = Loads.objects.get(id=self.object.id)
        #override ederek bu context i ekledik içine.
        return context
    