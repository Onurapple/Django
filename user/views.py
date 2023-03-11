from django.shortcuts import render

# Create your views here.
def contacts_page(request):
    return render(request, 'user/user.html')
