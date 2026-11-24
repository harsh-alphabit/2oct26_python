from django.shortcuts import render, redirect
from .models import ContactForm
from .forms import ContactUs

# Create your views here.

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == 'POST':
        contactusform=ContactUs(request.POST)
        if contactusform.is_valid():
            contactusform.save()
            print("massege got successfully")
        else:
            print(contactusform.errors)
        return redirect('contact')

    return render(request, 'contact.html')

def features(request):
    return render(request, 'features.html')

def qoute(request):
    return render(request,'qoute.html')

def service(request):
    return render(request,'service.html')

def team(request):
    return render(request,'team.html')

def testimonial(request):
    return render(request,'testimonial.html')