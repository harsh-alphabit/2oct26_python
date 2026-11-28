# DBMS and ORM: simple CRUD theory

This lesson explains what the database does underneath the CRUD pages in `module-10/dbproject`. Read [ORM_BEFORE_AFTER.md](ORM_BEFORE_AFTER.md) for the changes from the earlier version, and [ORM_THEORY.md](ORM_THEORY.md) for more query methods.

## 1. Database, table, row, and column

A **database** stores data. A **table** groups records of one kind. Each **row** is one record; each **column** holds one kind of value.

The current model, `user_signup` in `stdata/models.py`, corresponds to the database table `stdata_user_signup`:

| id | name | email | mobile | address |
| --- | --- | --- | --- | --- |
| 1 | Asha | a@b.co | 1234567890 | City |
| 2 | Ravi | r@b.co | 9876543210 | Town |

This is example data. The table also has a `password` column, which is left out of the examples because a password should not be displayed in a list. In this classroom project, that field currently stores plain text; it is not a real account system.

A **DBMS** is the software that manages the database. This project uses SQLite. Django's **ORM** lets our Python code ask that DBMS to read or change rows. Django still sends SQL to the database behind the scenes.

## 2. Models and migrations

```python
class user_signup(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=12)
    mobile = models.BigIntegerField()
    address = models.TextField()
```

The **model** describes the table in Python. Each field describes a column. The real model also has `password`, and Django adds an `id` primary key because we did not define another one.

Changing a model file does not immediately change the database table. `makemigrations` prepares a description of the change; `migrate` applies it to the database. Module 10's migrations have already been applied.

## 3. Keys: how rows are identified and connected

A **key** is a column, or a group of columns, used to identify a row or connect tables.

| Key | Simple meaning | Example |
| --- | --- | --- |
| Primary key (PK) | The chosen unique ID for each row | `user_signup.id` in this project |
| Foreign key (FK) | A value pointing to another table's row | A possible `Submission.student_id` pointing to `user_signup.id` |
| Unique key | A rule that forbids repeated values | `email` **would** be unique if its model field had `unique=True`; it does not now |
| Candidate key | A smallest set of columns that could uniquely identify a row | The `id` column is one candidate here |
| Super key | Any set of columns that uniquely identifies a row, even if it has extra columns | `(id, name)` is a super key because `id` already identifies the row |
| Alternate key | A candidate key that was not chosen as the primary key | Only exists if there is another candidate key |
| Composite key | A key made from multiple columns | A pair such as `(student_id, course_id)` could identify one enrolment |
| Surrogate key | An ID created only to identify rows | Django's automatic numeric `id` |
| Natural key | A real-world value used to identify a row | Email *might* be used, but this project's email field is not unique |

`name`, `email`, and `mobile` are **not unique** in the current model, so do not assume they identify exactly one record. This project has no foreign key yet. The FK and JOIN examples below show what a later relationship lesson could add.

## 4. CRUD: INSERT, SELECT, UPDATE, DELETE

CRUD means **Create, Read, Update, Delete**. SQL calls these operations `INSERT`, `SELECT`, `UPDATE`, and `DELETE`.

| Website action | ORM in `stdata/views.py` | SQL idea |
| --- | --- | --- |
| Submit the signup form | `user_signup.objects.create(...)` | `INSERT` a new row |
| Open View Data | `user_signup.objects.all().order_by('-id')` | `SELECT` rows and `ORDER BY id DESC` |
| Submit Edit | Change `data` fields, then `data.save()` | `UPDATE` the row with that ID |
| Confirm Delete | `data.delete()` | `DELETE` the row with that ID |

### Create: INSERT

```python
user_signup.objects.create(name='Asha', email='a@b.co', password='demo', mobile=1234567890, address='City')
```

Conceptual SQL:

```sql
INSERT INTO stdata_user_signup (name, email, password, mobile, address)
VALUES ('Asha', 'a@b.co', 'demo', 1234567890, 'City');
```

The database gives the new row an `id`. The website checks form data first, then calls `objects.create()`. Calling `create()` saves immediately; there is no second `save()` step.

### Read: SELECT, WHERE, and ORDER BY

```python
user_signup.objects.all()                       # All rows.
user_signup.objects.filter(name='Asha')         # Matching rows only.
user_signup.objects.order_by('-id')             # Highest IDs first.
```

Conceptual SQL for the filtered query:

```sql
SELECT * FROM stdata_user_signup WHERE name = 'Asha';
```

`filter()` can return zero, one, or many rows. `get(id=3)` expects exactly one row and raises an error if it cannot find one. The Edit and Delete views use `get_object_or_404(user_signup, id=id)`: Django uses the ORM to find that row and displays a 404 page if it is missing.

### Update: UPDATE

```python
data = user_signup.objects.get(id=3)
data.name = 'Asha Patel'  # Only the Python object has changed so far.
data.save()               # Write the change to the database.
```

Conceptual SQL:

```sql
UPDATE stdata_user_signup SET name = 'Asha Patel' WHERE id = 3;
```

The actual SQL produced by `save()` may include other fields too; the example shows the main idea. Django also has `user_signup.objects.filter(id=3).update(name='Asha Patel')` for a direct database update. The current Edit page uses `save()` so students can see the object change first.

### Delete: DELETE

```python
data = user_signup.objects.get(id=3)
data.delete()
```

Conceptual SQL:

```sql
DELETE FROM stdata_user_signup WHERE id = 3;
```

The website first shows a confirmation page. Opening the Delete link is a **GET** request and does not remove anything. Clicking **Yes, delete** sends a **POST** request; that is when `delete()` runs. Use an ID from disposable practice data when trying the shell examples above.

## 5. JOIN: reading related tables

A **JOIN** combines rows from two tables through a matching key. **The current project has only one lesson table and does not implement this relationship.** Imagine that a future `Submission` model has a foreign key to `user_signup`:

```python
class Submission(models.Model):
    student = models.ForeignKey(user_signup, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
```

The submission table would have `student_id`, which stores the student's `id`. To find submissions by a student's name:

```python
Submission.objects.filter(student__name='Asha')
```

`student__name` tells Django to follow the foreign key and compare the related student's name. Django makes the needed SQL JOIN. The SQL idea is:

```sql
SELECT s.*
FROM stdata_submission AS s
JOIN stdata_user_signup AS u ON s.student_id = u.id
WHERE u.name = 'Asha';
```

If a page also displays `submission.student.name` for many submissions, `Submission.objects.select_related('student')` can fetch each submission and its student in one query. A `OneToOneField` links one row to at most one related row. A `ManyToManyField` connects rows through an extra join table. These are later lessons; no such models were added here.

## 6. What a form, ORM, and DBMS each do

When a student submits the form, the flow is:

1. **HTML form:** collects text and sends a POST request.
2. **`userForm`:** checks field rules and gives the view `cleaned_data`.
3. **View:** decides whether to create, update, read, or delete.
4. **ORM:** turns the view's model operations into database queries.
5. **DBMS:** stores or returns the rows.
6. **Template:** shows the returned data in the browser.

The form and the ORM do different jobs. `userForm` checks submitted values. `objects.create()`, `filter()`, `save()`, and `delete()` work with the database. The earlier `userForm.save()` also used the ORM internally; the current view shows those steps explicitly for learning.

## 7. ORM compared with writing SQL yourself

| Question | ORM | Raw SQL |
| --- | --- | --- |
| How do I ask for Asha's rows? | `user_signup.objects.filter(name='Asha')` | `SELECT ... WHERE name = 'Asha'` |
| What do I work with in Python? | Model objects or QuerySets | Database rows returned by a cursor |
| How are relationships followed? | `student__name` and model relationships | Write the JOIN condition yourself |
| Do I still need to understand tables and keys? | Yes | Yes |
| Is it automatically faster? | No | No |

The ORM makes common queries readable alongside the Python model code and lets Django handle many SQL details. Raw SQL remains useful for queries that the ORM cannot express clearly. Either approach can be slow if you ask for too much data or repeat queries unnecessarily. The benefit of the current rewrite over the first version is **visibility for students**: the first version already used ORM through `ModelForm.save()`.

## 8. A few DBMS rules to remember

- A **constraint** is a database rule. The primary key must identify a row uniquely. `unique=True` would make a field unique, but this model does not put it on email.
- A **transaction** groups several database writes so they all succeed or all roll back. The current CRUD pages make one main write per request; a later multi-step workflow could use `transaction.atomic()`.
- A QuerySet can be filtered and sorted before Django fetches its rows. `count()` asks for a number; `exists()` asks whether at least one row exists.
- The ORM does not automatically decide which rows a visitor is allowed to see. An application must add the right filters and access checks. This classroom list currently shows all its records.

## 9. Practise in module-10

From `module-10/dbproject`, run:

```text
..\myenv\Scripts\python.exe manage.py runserver
```

Use `/` to add one **practice** record, `/dbdata/` to read it, Edit to update it, and Delete to remove it. For read-only query examples, run:

```text
..\myenv\Scripts\python.exe manage.py orm_examples
```

Further reading: [Django queries](https://docs.djangoproject.com/en/6.0/topics/db/queries/), [model fields and keys](https://docs.djangoproject.com/en/6.0/ref/models/fields/), [migrations](https://docs.djangoproject.com/en/6.0/topics/migrations/), and [transactions](https://docs.djangoproject.com/en/6.0/topics/db/transactions/).
