from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import Contacts

# Create your views here.
def contacts_page(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        contact = form.save()
        return redirect('')
    context = {
        'form': form
    }
    return render(request, 'user/user.html', context)

def get_contacts(request):
    contacts = Contacts.objects.all()
    context = {
        'contacts': contacts
    }
    return render(request, 'user/user.html', context )

