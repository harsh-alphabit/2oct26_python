from django.shortcuts import render, redirect
from myapp.forms import UserForm
from myapp.models import User

# Create your views here.
def index(request):
    if request.method == 'POST':
        unm = request.POST.get('username')
        pwd = request.POST.get('password')
        user = User.objects.filter(username=unm, password=pwd)

        if user:
            print("Login successful")
            request.session['username'] = unm  #session create
            return redirect('home')
        else:
            print("Invalid username or password")
    return render(request, 'index.html')


def usersignup(request):
    if request.method == 'POST':
        signupdata = UserForm(request.POST)
        if signupdata.is_valid():
            signupdata.save()
            print("User created successfully")
            return redirect('home')
        else:
            print(signupdata.errors) 
    return render(request, 'usersignup.html')


def home(request):
    user = request.session.get('username')  #session get


    return render(request, 'home.html', {'user': user} )