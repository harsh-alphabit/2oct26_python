from django.shortcuts import render, redirect
from .models import ContactForm, QuoteRequest
from .forms import ContactUs, QuoteForm, SubscriberForm
from django.contrib import messages

# Create your views here.

def index(request):
    quoteform = QuoteForm()
    return render(request, 'index.html', {'form': quoteform})

def about(request):
    return render(request, 'about.html')

def contact(request):
    contactusform = ContactUs()
    if request.method == 'POST':
        contactusform=ContactUs(request.POST)
        if contactusform.is_valid():
            contactusform.save()
            print("message got successfully")
            return redirect('contact')

    return render(request, 'contact.html', {'form': contactusform})

def feature(request):
    return render(request, 'feature.html')

def quote(request):
    quoteform = QuoteForm()
    if request.method == 'POST':
        quoteform = QuoteForm(request.POST)
        if quoteform.is_valid():
            quoteform.save()
            messages.success(request, 'Your quote request has been submitted.')
            return redirect('quote')

    return render(request, 'quote.html', {'form': quoteform})

def service(request):
    return render(request,'service.html')

def team(request):
    return render(request,'team.html')

def testimonial(request):
    return render(request,'testimonial.html')


def search(request):
    q = request.GET.get('q', '').strip()
    #'q' is the input’s name. Django looks for q in a URL such as /search/?q=Cyber.
    #'' is the default: an empty string used when the URL has no q.
    results = []

    if q:
        for value, label in QuoteRequest.services:
            #quoterequest.services= services is the list you already wrote inside the QuoteRequest model
            if q.lower() in label.lower():
                results.append(label)

    return render(request, 'search.html', {'q': q, 'results': results})


def subscribe(request):
    if request.method == 'POST':
        form = SubscriberForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for subscribing.')
        else:
            messages.error(request, 'Enter a valid email address that is not already subscribed.')

    return redirect('/')
