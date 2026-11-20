from django.shortcuts import render, redirect
from stdata.forms import userForm
from stdata.models import user_signup

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
    data=user_signup.objects.all()
    return render(request, 'dbdata.html',{'data':data}) #context value


def update(request, id):
    data=user_signup.objects.get(id=id)
    if request.method == "POST":
        user=userForm(request.POST)
        if user.is_valid():
            user=userForm(request.POST, instance=data)   
            user.save()
            print("record updated")
            return redirect('dbdata')
        else:
            print(user.errors)
    return render(request, 'update.html', {'data':data})


def delete(request, id):
    data=user_signup.objects.get(id=id)
    data.delete()
    print("record deleted")
    return redirect('dbdata')