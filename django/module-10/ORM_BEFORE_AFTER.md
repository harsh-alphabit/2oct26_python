# Module 10: what changed, and why?

The first version of this project already used Django's ORM. For example, `user_signup.objects.all()` read rows, `user_signup.objects.get(id=id)` found one row, and `data.delete()` removed a row. `userForm.save()` also used the ORM internally.

The current version makes the **Create, Read, Update, and Delete** steps easier to see in `dbproject/stdata/views.py`. It keeps `userForm` to check submitted data, then calls the ORM methods in the view.

## Before and now

| Action | First version | Current version | What students can see now |
| --- | --- | --- | --- |
| Create | `userForm(request.POST)` followed by `form.save()` | Validate the form, then call `user_signup.objects.create(...)` | The line that adds a database row |
| Read | `user_signup.objects.all()` | `user_signup.objects.all().order_by('-id')` | All rows, with newest first |
| Update | `userForm(request.POST, instance=data).save()` | Change `data.name`, `data.email`, and other fields, then call `data.save()` | The difference between changing a Python object and saving it |
| Delete | `data.delete()` ran when the Delete link was opened | Open a confirmation page; `data.delete()` runs only after submitting its form | The exact point when the row is removed |

The first version's `objects.get(id=id)` would raise an error if the ID did not exist. The current version uses `get_object_or_404(user_signup, id=id)`, which finds one row through the ORM and shows a normal 404 page when it is missing.

## Flow: Create a record

1. The student fills in the form on `/` and clicks **Signup**.
2. The browser sends a **POST** request with those fields.
3. `userForm(request.POST)` checks the field rules. `form.is_valid()` tells us if they passed.
4. `form.cleaned_data` contains the checked values.
5. `user_signup.objects.create(...)` inserts one row into the database.
6. `redirect('dbdata')` opens the list page, where the new row appears.

If the form is invalid, the page shows its errors and does not create a row.

## Flow: Read records

1. The browser opens `/dbdata/` with a **GET** request.
2. `user_signup.objects.all().order_by('-id')` describes the rows to fetch and their order.
3. `render()` sends `data` to `dbdata.html`.
4. The template's `{% for i in data %}` loop displays one table row per record.

## Flow: Update a record

1. The student clicks **Edit** for a record. Its ID is in the URL, such as `/update/3/`.
2. `get_object_or_404()` finds that record and shows its values in the form.
3. The student submits the form. `userForm` checks the new values.
4. The view assigns the new values to `data.name`, `data.email`, and the other fields. At this point, they are changed in the Python object.
5. `data.save()` writes those changes to the database, and the browser returns to the list.

Leaving the password input empty on the Edit page keeps its current value. The page no longer prints that value into the input.

## Flow: Delete a record

1. The student clicks **Delete** to open a confirmation page. This **GET** request only displays the page.
2. The student clicks **Yes, delete**. The browser sends a **POST** request with a CSRF token.
3. `data.delete()` removes the row, then the view redirects to the list.

## Why use ORM?

Without an ORM, we would have to write database commands such as `SELECT`, `INSERT`, `UPDATE`, and `DELETE` ourselves. The ORM lets us express these operations with Python objects and methods:

```python
user_signup.objects.filter(name='Asha')  # Find matching rows.
data.name = 'Asha Patel'                    # Change one Python object.
data.save()                                 # Write that change to the database.
```

In **this project's before-and-after comparison**, the main benefit is **clearer teaching and more control over each step**. The old `ModelForm.save()` was already using the ORM. The new code is longer and is not automatically faster. For simple forms, `ModelForm.save()` remains a good option after students understand what it does.

Next, read [ORM_THEORY.md](ORM_THEORY.md) for common query methods, or run `..\myenv\Scripts\python.exe manage.py orm_examples` from `module-10/dbproject` to see read-only examples.
