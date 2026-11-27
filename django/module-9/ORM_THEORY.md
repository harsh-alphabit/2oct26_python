# Django ORM: simple theory

## What is ORM?

**ORM** stands for **Object-Relational Mapping**. It lets us work with database records using Python classes and methods. Django converts our ORM code into database queries.

For example:

```python
QuoteRequest.objects.filter(status='Pending')
```

This means: **find quotations whose status is Pending**. We do not have to write the SQL query ourselves.

## What do the words mean?

| Word | Simple meaning | Example in our project |
| --- | --- | --- |
| Model | A Python class that describes data we want to store | `QuoteRequest` |
| Field | One piece of data in a model | `status`, `service`, `total_price` |
| Object | One saved record | One customer's quotation |
| `objects` | Django's starting point for database queries | `QuoteRequest.objects` |
| QuerySet | A group of records returned by a query | All Pending quotations |

Think of a database table as a spreadsheet: fields are columns, and each saved object is a row. This is only an analogy; Django still uses a real database.

## Reading a query from left to right

```python
QuoteRequest.objects.filter(customer=customer).order_by('-id')
```

1. `QuoteRequest`: use the quotation model.
2. `.objects`: start a database query.
3. `.filter(customer=customer)`: keep this customer's quotations.
4. `.order_by('-id')`: put the highest IDs first, which is newest first in this project.

The dashboard uses this query so a customer sees their own quotations.

## Common ORM methods

| Method | What it does | Example |
| --- | --- | --- |
| `all()` | Gets every record | `QuoteRequest.objects.all()` |
| `filter()` | Gets records that match | `QuoteRequest.objects.filter(status='Pending')` |
| `exclude()` | Gets records that do **not** match | `QuoteRequest.objects.exclude(status='Rejected')` |
| `order_by()` | Sorts records | `QuoteRequest.objects.order_by('-id')` |
| `first()` | Gets one record, or `None` if there is none | `QuoteRequest.objects.first()` |
| `get()` | Gets exactly one record | `QuoteRequest.objects.get(id=1)` |
| `count()` | Returns the number of matching records | `QuoteRequest.objects.filter(status='Pending').count()` |
| `exists()` | Returns `True` if at least one record matches | `QuoteRequest.objects.filter(status='Pending').exists()` |

`get(id=1)` works only when quote 1 exists. If nothing matches, `get()` raises an error. `filter()` can safely return an empty QuerySet, and `first()` can return `None`.

## What happens when we save data?

```python
quote = QuoteRequest.objects.get(id=1)
quote.status = 'Approved'
quote.save()
```

`get()` reads the record. Changing `quote.status` changes the Python object. `save()` writes that change to the database. Use an ID that exists in your database when trying this example.

To create a new record, the project uses `QuoteRequest.objects.create(...)`. Django saves the new object immediately. To remove a record, the project calls `quote.delete()`.

## How are models connected?

`QuoteRequest` has a `customer` field that points to a `Customer`. This is a **ForeignKey**: one customer can have many quotations, and each quotation belongs to one customer.

```python
QuoteRequest.objects.filter(customer=customer)
```

This asks for that customer's quotations. On the website, always start with the logged-in customer when showing or changing their quotations.

## Where to practise

Open a terminal in `module-9/startup` and run:

```text
..\myenv\Scripts\python.exe manage.py shell
```

Then run:

```python
from myapp.models import QuoteRequest
QuoteRequest.objects.all()
```

See [ORM_LESSON.md](ORM_LESSON.md) for a step-by-step exercise using all the methods above.
