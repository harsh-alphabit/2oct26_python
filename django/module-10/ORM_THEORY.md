# Django ORM: theory and common queries

This lesson uses the `user_signup` model in `dbproject/stdata/models.py`. It is a classroom data table. Use sample records when practising.

For the difference from the first version of this project, see [ORM_BEFORE_AFTER.md](ORM_BEFORE_AFTER.md).

## 1. What is ORM?

**ORM** means **Object-Relational Mapping**. Django lets us write Python code to work with database tables. Django turns the ORM code into database queries.

```python
user_signup.objects.all()
```

Read this as: “Get all records from the `user_signup` table.”

| Term | Simple meaning | In this project |
| --- | --- | --- |
| Model | Python class that describes a table | `user_signup` |
| Field | One column in the table | `name`, `email`, `mobile` |
| Object | One row returned as a Python object | One signup record |
| `objects` | Django's starting point for queries | `user_signup.objects` |
| QuerySet | A group of rows described by a query | Results from `.all()` or `.filter()` |

The spelling `user_signup` is the name already used in this project. Many Django projects use `UserSignup` for a model class, but the ORM works with either name.

## 2. CRUD: changing records

CRUD means **Create, Read, Update, Delete**. These actions are implemented in `dbproject/stdata/views.py`:

```python
# Create one row and save it immediately.
user_signup.objects.create(name='Asha', email='a@b.co', password='demo', mobile=1234567890, address='City')

# Read rows, newest first.
user_signup.objects.all().order_by('-id')

# Update one object after reading it.
record = user_signup.objects.first()
if record:
    record.name = 'Asha Patel'
    record.save()

# Delete one object after reading it.
record = user_signup.objects.first()
if record:
    record.delete()
```

**Do not run the Update or Delete shell examples on a record you want to keep.** The website's Edit and Delete pages let you practise with a record you choose. The website also validates form data before creating or updating a row.

## 3. Reading records

Open Django shell from `module-10/dbproject`:

```text
..\myenv\Scripts\python.exe manage.py shell
```

Then import the model:

```python
from stdata.models import user_signup
```

| Method | Simple meaning | Example |
| --- | --- | --- |
| `all()` | All records | `user_signup.objects.all()` |
| `filter()` | Only matching records | `user_signup.objects.filter(name='Asha')` |
| `exclude()` | Everything except matches | `user_signup.objects.exclude(name='Asha')` |
| `get()` | Exactly one record | `user_signup.objects.get(id=1)` |
| `first()` | First record, or `None` | `user_signup.objects.order_by('id').first()` |
| `last()` | Last record, or `None` | `user_signup.objects.order_by('id').last()` |
| `count()` | Number of records | `user_signup.objects.count()` |
| `exists()` | `True` if any record matches | `user_signup.objects.filter(name='Asha').exists()` |

`filter()` always returns a QuerySet, even if it has no rows. `get()` returns one object, but raises an error when there is no match or more than one match. Use a real ID from your database when trying `get(id=...)`.

## 4. Conditions and lookups

The part after `__` tells Django **how to compare** a field:

```python
user_signup.objects.filter(name='Asha')                # Exact match.
user_signup.objects.filter(name__icontains='ash')      # Contains 'ash', ignoring case.
user_signup.objects.filter(name__startswith='A')       # Starts with A.
user_signup.objects.filter(id__gt=2)                   # ID greater than 2.
user_signup.objects.filter(id__gte=2)                  # ID greater than or equal to 2.
user_signup.objects.filter(id__in=[1, 2, 3])           # ID is in this list.
```

Two conditions in one `filter()` mean **AND**:

```python
user_signup.objects.filter(name__icontains='a', id__gt=2)
```

For **OR**, use `Q`:

```python
from django.db.models import Q

user_signup.objects.filter(Q(name__icontains='a') | Q(address__icontains='city'))
```

## 5. Sorting, chaining, and limiting

```python
user_signup.objects.order_by('name')                    # Name A to Z.
user_signup.objects.order_by('-id')                     # Highest ID first.
user_signup.objects.filter(name__icontains='a').order_by('name')
user_signup.objects.order_by('-id')[:2]                 # Only two newest records.
```

You can join QuerySet methods together. A QuerySet describes a query; Django normally waits until you use its results before fetching the rows. `count()` and `exists()` ask the database for their answers directly.

## 6. Choosing fields and removing duplicates

```python
user_signup.objects.values('id', 'name')                # Dictionaries with these fields.
user_signup.objects.values_list('name', flat=True)      # Just the names.
user_signup.objects.order_by().values_list('address', flat=True).distinct()
```

`values()` is useful when you need selected fields instead of full model objects. `distinct()` removes repeated results. The empty `order_by()` clears ordering before asking for distinct addresses.

## 7. Summaries

```python
from django.db.models import Count, Max

user_signup.objects.aggregate(total=Count('id'), highest_id=Max('id'))
user_signup.objects.values('address').annotate(total=Count('id')).order_by('address')
```

`aggregate()` gives **one summary for the whole query**. `annotate()` adds a calculated value to each result. Here, `values('address')` makes one group per address, and `Count('id')` counts records in each group.

## 8. `save()` versus QuerySet `update()`

The website edits one object and calls `save()`. Django also has `update()` for changing many matching rows in one query:

```python
user_signup.objects.filter(address='Old City').update(address='New City')
```

`update()` changes **every matching row**. Similarly, `user_signup.objects.filter(address='Old City').delete()` removes every matching row. Practise these on disposable sample data only. For this beginner CRUD page, `record.save()` and `record.delete()` are easier to follow.

## 9. Run the read-only examples

From `module-10/dbproject`:

```text
..\myenv\Scripts\python.exe manage.py orm_examples
```

The command shows the common read queries using your saved records. It does **not** create, update, or delete any record. To practise the four write actions, use the website and [ORM_CRUD.md](ORM_CRUD.md).

This model has no `ForeignKey`, so relationship queries such as `select_related()` are a later lesson, after adding a second related model.

Further reading: [Django query guide](https://docs.djangoproject.com/en/6.0/topics/db/queries/), [QuerySet reference](https://docs.djangoproject.com/en/6.0/ref/models/querysets/), and [aggregation guide](https://docs.djangoproject.com/en/6.0/topics/db/aggregation/).
