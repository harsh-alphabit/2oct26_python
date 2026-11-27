# ORM lesson: practise with quotations

ORM lets us read database records with Python instead of writing SQL. The model is `QuoteRequest`, and `objects` is Django's manager for querying its table.

## 1. Make some example quotations

Use the website to create a few quotations. Change some of their statuses to Approved or Rejected in Django admin. The examples below are easier to see when the database has more than one quote.

## 2. Open Django shell

Open a terminal in `module-9/startup` and run:

```text
..\myenv\Scripts\python.exe manage.py shell
```

Then import the models:

```python
from myapp.models import QuoteRequest, Customer
```

## 3. Try one ORM method at a time

```python
# all() gets every quotation.
QuoteRequest.objects.all()

# filter() keeps only rows that match a condition.
QuoteRequest.objects.filter(status='Pending')

# exclude() leaves out rows that match a condition.
QuoteRequest.objects.exclude(status='Rejected')

# order_by() sorts the rows. The minus sign means descending order.
QuoteRequest.objects.order_by('-id')

# count() returns the number of matching rows.
QuoteRequest.objects.filter(status='Approved').count()

# exists() returns True or False: is there at least one matching row?
QuoteRequest.objects.filter(status='Pending').exists()

# first() returns one row, or None if the table is empty.
quote = QuoteRequest.objects.first()
print(quote)

# get() returns exactly one row. Use a real ID from the database.
# If no row matches, get() raises an error; first() would return None.
if quote:
    QuoteRequest.objects.get(id=quote.id)
```

`all()`, `filter()`, `exclude()`, and `order_by()` return a **QuerySet**: a group of database rows that you can loop over. `first()` and `get()` return one object. `count()` returns a number. `exists()` returns `True` or `False`.

## 4. Use the customer relationship

`QuoteRequest.customer` links each quotation to a customer. Try this after at least one customer has signed up:

```python
customer = Customer.objects.first()
if customer:
    QuoteRequest.objects.filter(customer=customer)
```

This is the same idea used in the dashboard view:

```python
quotes = QuoteRequest.objects.filter(customer=customer).order_by('-id')
```

Read it from left to right: **start with quotations → keep this customer's quotations → show newest first**. The dashboard sends `quotes` to `dashboard.html`, where `{% for quote in quotes %}` makes a table row for each one.

## 5. Student practice

1. Show all Approved quotations.
2. Show all quotations except Rejected ones.
3. Count Pending quotations.
4. Show the newest quotation.
5. Check whether any Rejected quotation exists.
6. Show the quotations belonging to one customer.

These shell queries are for learning. The website dashboard must continue to filter by the logged-in customer so one customer cannot see another customer's quotations.
