from django.shortcuts import render, redirect
from myapp.forms import userForm

def index(request):
    if request.method == "POST": #true
        user=userForm(request.POST)
        if user.is_valid(): #true
            user.save()
            print("your account has been created")
            return redirect('dbdata')
        else:
            print(user.errors)
    return render(request, 'index.html')



def dbdata(request):
    return render(request, 'dbdata.html')