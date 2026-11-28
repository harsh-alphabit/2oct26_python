# How to implement ORM in this Django project

Django's ORM is already included with Django. You do **not** install a separate ORM package. This guide follows the working files in `module-10/dbproject` so you can build and explain the same CRUD flow in class.

## Step 1: Choose the data to store

This project stores student signup records. The model is `user_signup` in `stdata/models.py`. Its fields are `name`, `email`, `password`, `mobile`, and `address`. Django also gives each record an automatic `id` primary key.

The project uses SQLite, configured in `dbproject/settings.py`. `stdata` must be present in `INSTALLED_APPS` so Django can find its model and migrations.

> This is a classroom CRUD example. Its current password field stores plain text and should not be used as a real account system.

## Step 2: Write the model

A model is the Python description of a database table:

```python
from django.db import models

class user_signup(models.Model):
    name = models.CharField(max_length=100)
    password = models.CharField(max_length=20)
    email = models.EmailField(max_length=12)
    mobile = models.BigIntegerField()
    address = models.TextField()
```

One saved `user_signup` object becomes one row. Each model field becomes a column. Open `stdata/models.py` to see the full current model, including its `__str__()` method.

## Step 3: Create the database table

In a terminal opened in `module-10/dbproject`, run:

```text
..\myenv\Scripts\python.exe manage.py makemigrations stdata
..\myenv\Scripts\python.exe manage.py migrate
```

`makemigrations` records the planned table change. `migrate` applies it to `db.sqlite3`. The migrations for this project have already been run; use these commands again after changing a model.

## Step 4: Add a form for checking input

The project defines `userForm` in `stdata/forms.py`:

```python
class userForm(forms.ModelForm):
    class Meta:
        model = user_signup
        fields = '__all__'
```

The HTML in `templates/index.html` contains ordinary `<input>` fields. On POST, `userForm(request.POST)` checks them. Only when `form.is_valid()` is true does the view use `form.cleaned_data` to create a row.

**Form and ORM have different jobs:** the form checks input; the ORM reads and writes database rows. In this lesson, the view calls ORM methods explicitly so students can see them.

## Step 5: Write the four views

The working code is in `stdata/views.py`. These are its important ORM lines:

### Create

```python
if request.method == 'POST' and form.is_valid():
    values = form.cleaned_data
    user_signup.objects.create(
        name=values['name'],
        email=values['email'],
        password=values['password'],
        mobile=values['mobile'],
        address=values['address'],
    )
```

`objects.create()` makes a new object **and saves it immediately**. The working view calls this after checking the form, then redirects to the list page.

### Read

```python
data = user_signup.objects.all().order_by('-id')
```

`all()` asks for the saved rows. `order_by('-id')` puts the highest IDs first. The view sends `data` to `templates/dbdata.html`, where a `{% for i in data %}` loop displays the rows.

### Update

```python
data = get_object_or_404(user_signup, id=id)
data.name = values['name']
data.save()
```

The URL supplies `id`. `get_object_or_404()` finds that row using the ORM or shows a 404 page. The working view checks all submitted fields, assigns their new values, then calls `save()` **once** to write them. Leaving the Edit page's password input empty keeps the current value.

### Delete

```python
data = get_object_or_404(user_signup, id=id)
if request.method == 'POST':
    data.delete()
```

Opening the Delete page only shows a confirmation. `delete()` runs after the confirmation form sends a POST request.

## Step 6: Connect URLs to views

`stdata/urls.py` connects paths to the four view functions:

| Path | View | Action |
| --- | --- | --- |
| `/` | `index` | Create |
| `/dbdata/` | `dbdata` | Read |
| `/update/<id>/` | `update` | Update |
| `/delete/<id>/` | `delete` | Confirm and delete |

`dbproject/urls.py` includes `stdata.urls`. Named URLs such as `{% url 'update' i.id %}` in the template build the correct link for a record.

## Step 7: Show and submit data in templates

- `templates/index.html`: form for a new record. It uses `method="POST"` and `{% csrf_token %}`.
- `templates/dbdata.html`: loops over `data` and shows Edit and Delete links for each row.
- `templates/update.html`: shows the record's current values and submits changes with POST.
- `templates/delete.html`: asks for confirmation and sends POST only when the user confirms.

When a form has invalid values, the Create and Update pages show `form.errors` instead of saving a row.

## Step 8: Follow one request from start to finish

```text
Student fills in HTML form
        ↓ POST
URL selects a view
        ↓
ModelForm checks the submitted data
        ↓ valid
ORM create(), save(), or delete() changes the database
        ↓ redirect
List view uses ORM all() to read saved rows
        ↓
Template displays the rows
```

For a GET request to the list page, there is no form submission: the view simply reads rows and renders the template.

## Step 9: Run and check the flow

From `module-10/dbproject`:

```text
..\myenv\Scripts\python.exe manage.py runserver
```

Try this sequence: add a practice record → see it on `/dbdata/` → edit its name → see the new name → open Delete → cancel once → reopen and confirm. This checks all four CRUD actions.

To practise more read queries without changing records, run:

```text
..\myenv\Scripts\python.exe manage.py orm_examples
```

For the DBMS meaning of keys, SQL commands, and JOINs, read [ORM_CRUD.md](ORM_CRUD.md). For common query methods, read [ORM_THEORY.md](ORM_THEORY.md).
