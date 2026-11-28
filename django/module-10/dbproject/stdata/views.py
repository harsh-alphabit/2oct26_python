from django.shortcuts import render, redirect, get_object_or_404
from stdata.forms import userForm
from stdata.models import user_signup


def index(request):
    # CREATE: show an empty form, or check the submitted values.
    form = userForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        data = form.cleaned_data
        # objects.create() adds one new row to the database.
        user_signup.objects.create(
            name=data['name'],
            email=data['email'],
            password=data['password'],
            mobile=data['mobile'],
            address=data['address'],
        )
        return redirect('dbdata')

    return render(request, 'index.html', {'form': form})


def dbdata(request):
    # READ: all() gets all saved rows; order_by() shows newest first.
    data = user_signup.objects.all().order_by('-id')
    return render(request, 'dbdata.html', {'data': data})


def update(request, id):
    # get_object_or_404() gets one row by ID, or shows a 404 page.
    data = get_object_or_404(user_signup, id=id)
    if request.method == 'POST':
        submitted = request.POST.copy()
        # Leaving password empty means keep the current value.
        if not submitted.get('password'):
            submitted['password'] = data.password
        form = userForm(submitted, instance=data)
    else:
        form = userForm(instance=data)

    if request.method == 'POST' and form.is_valid():
        values = form.cleaned_data
        # UPDATE: change the object, then save() writes those changes.
        data.name = values['name']
        data.email = values['email']
        data.password = values['password']
        data.mobile = values['mobile']
        data.address = values['address']
        data.save()
        return redirect('dbdata')

    return render(request, 'update.html', {'data': data, 'form': form})


def delete(request, id):
    data = get_object_or_404(user_signup, id=id)
    if request.method == 'POST':
        # DELETE: delete() removes the row after the confirmation form is sent.
        data.delete()
        return redirect('dbdata')

    return render(request, 'delete.html', {'data': data})
