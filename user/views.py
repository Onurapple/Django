from django.shortcuts import render, redirect
from .forms import ContactForm
from .models import Contacts

# Create your views here.
def contacts_create_list(request):
    contacts = Contacts.objects.all()
    form = ContactForm()
    print(request.POST)
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('contacts_create_list')
    context = {
        'form': form,
        'contacts': contacts
    }
    return render(request, 'user/user.html', context)

def contact_update(request, id):
    contact=Contacts.objects.get(id=id)
    updateform = ContactForm(instance=contact)
    if request.method == 'POST':
        updateform=ContactForm(request.POST, instance=contact)
        if updateform.is_valid():
            updateform.save()
            return redirect('contacts_create_list')
    
    context={
        'updateform':updateform,
        'id':id
    }
    return render(request, 'user/user.html', context)

def contact_delete(request, id):
    deletecontact=Contacts.objects.get(id=id)
    if request.method == 'POST':
        deletecontact.delete()
        return redirect('contacts_create_list')

    context={
        'deletecontact':deletecontact
    }
    return render(request, 'user/user.html', context)

# def get_contacts(request):
#     contacts = Contacts.objects.all()
#     context = {
#         'contacts': contacts
#     }
#     return render(request, 'user/user.html', context )

