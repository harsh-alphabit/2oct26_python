from django.shortcuts import render
import random

# Create your views here.

def index(request):
    dt={'num':random.randint(1111,9999)}
    #return render(request,'index.html',{'name':'harsh'})
    return render(request,'index.html',dt)


def contact(request):
    return render(request,'contact.html')

def about(request):
    return render(request,'about.html')