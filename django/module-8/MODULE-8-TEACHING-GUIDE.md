# Module 8: Customer Login and Quotation Project

This guide explains **what to build first, why each part is needed, and how the finished project works**. It is written for students who are new to Django backend development.

## What students will build

A customer can sign up, sign in, choose a service, select work, get an estimated bill, and manage their quotations. An admin can view customers and quotations and mark a quotation Pending, Approved, or Rejected.

The prices are **sample classroom prices**. A quotation bill shows an estimate. It does not take a payment or prove that a payment was made.

## First understand the Django flow

```text
Browser link or form
       ↓
URL in myapp/urls.py
       ↓
Function in myapp/views.py
       ↓
Model/database, when data must be read or saved
       ↓
HTML template shown to the customer
```

For example, clicking **New Quotation** follows `/quote/` → `quote()` → `quote.html`.

| Part | Simple meaning | Why it is needed |
| --- | --- | --- |
| Model | Describes what data to save | So quotations and customers remain after closing the browser |
| Migration | Applies model changes to the database | A new model field does not create a database column by itself |
| URL | Connects a web address to a view | So Django knows which function to run |
| View | Handles the request and decides what happens | This is where login, validation, totals, and saving happen |
| Template | The HTML page the visitor sees | To show forms, messages, tables, and bills |
| Admin registration | Makes a model visible in Django admin | So staff can review saved records |

## Build it in this order

### Step 1 — Start with the existing Startup website

The pages already use `base.html` for the shared navbar, footer, and page blocks. Module 8 adds customer and quotation features to this website. Keep the existing pages working before adding the new flow.

**Why first?** Students can focus on backend logic instead of rebuilding the frontend.

### Step 2 — Make the `Customer` model

In `startup/myapp/models.py`, `Customer` stores first name, last name, phone number, email, and a password **hash**. Email is unique, so one email cannot belong to two customers.

**Why?** The project needs a customer record to know who owns each quotation. This website uses its own simple `Customer` model. The Django admin still uses Django's separate built-in admin accounts.

After adding or changing model fields, run these commands from `module-8/startup`:

```powershell
..\myenv\Scripts\python.exe manage.py makemigrations
..\myenv\Scripts\python.exe manage.py migrate
```

`makemigrations` writes the plan for the database change. `migrate` applies that plan.

### Step 3 — Add signup and signin pages

Add URLs such as `/signup/` and `/login/`, views named `signup()` and `user_login()`, and their matching templates. Each HTML input has a `name`, such as `name="email"`. The view reads it with `request.POST.get('email', '')` when the form is submitted.

Signup checks that required fields are present, the phone contains digits, and the email is not already used. `customer.full_clean()` checks the model's field rules before `customer.save()` writes the row. `make_password(password)` saves a password hash instead of the plain password.

Signin looks up the customer by email and uses `check_password()` to compare the typed password with the stored hash. Do not compare the typed password directly with the hash.

**Why?** A customer must have an identity before the project can attach a quotation to that customer.

### Step 4 — Remember who signed in

After a successful signup or signin, the view saves the customer ID in the session:

```python
request.session['customer_id'] = customer.id
```

Think of a session as a small piece of data Django remembers for this browser. `customer_id` is a key **we chose**. Django creates the session's own ID automatically, but it does not automatically know which `Customer` should be stored in our custom login flow. `request.session.cycle_key()` gives the session a new ID at login.

Protected views read the saved ID, find the customer, and send visitors without a valid customer to `/login/`. The dashboard, service menu, edit page, delete page, and bill all do this check. `logout(request)` clears the session and sends the customer back to the homepage.

**Why?** Without the session, the next page would not know which customer signed in.

### Step 5 — Connect a quotation to its customer

`QuoteRequest` has a `customer` field using `ForeignKey`. One customer can own many quotations. A quotation belongs to one customer.

```text
Customer A → Quote 1, Quote 2
Customer B → Quote 3
```

The view saves the current customer with the new quotation. When opening an existing quotation, it looks up **both** the quotation ID and the current customer:

```python
get_object_or_404(QuoteRequest, id=id, customer=customer)
```

**Why?** Knowing a quotation's number should not let Customer B open or change Customer A's quotation. Older quotations made before customer accounts were added may have no customer; they remain visible in admin.

### Step 6 — Create the service menu

`SERVICES` in `startup/myapp/views.py` lists the five services. Each service contains feature codes, names, and sample prices. For example:

```python
('website', 'Five-page website', 12000)
```

`website` is the value sent by the form, `Five-page website` is the text shown to people, and `12000` is the sample price. `/quote/` displays service cards in `quote.html`. Choosing a card opens `/quote/new/<service>/` and the form in `quote_service.html`.

**Why?** Customers first choose a service, then choose the work within that service. This replaces the old generic “contact us for a quote” form.

### Step 7 — Create and calculate the quotation

Each feature is a checkbox with `name="features"`. Several checkboxes can have the same name, so the view reads all checked values with:

```python
selected = request.POST.getlist('features')
```

The view checks that at least one feature was selected, that every code belongs to this service, and that the same code was not sent twice. It then adds the **server-side** prices, creates a `QuoteRequest`, and saves the feature codes, total, customer, and optional extra details.

**Why calculate in the view?** The browser sends selected feature codes; it must not be trusted to supply the final price. After saving, Django redirects to the new quotation's bill.

### Step 8 — Show the bill and dashboard

`quote_bill.html` displays the quotation number, date, customer, service, selected work, item prices, total estimated price, and status. **Print Bill** opens the browser's print dialog.

`dashboard()` loads only the signed-in customer's quotations:

```python
QuoteRequest.objects.filter(customer=customer).order_by('-id')
```

The dashboard shows the latest quotation first, with links to view its bill, edit it, or delete it.

**Why?** Saving a quotation is useful only if customers can return to it later.

### Step 9 — Add edit and delete: complete CRUD

CRUD means **Create, Read, Update, Delete**.

| Letter | What the customer does here | Django view |
| --- | --- | --- |
| Create | Selects features and generates a quotation | `create_quote()` |
| Read | Views the dashboard or bill | `dashboard()`, `quote_bill()` |
| Update | Changes features or extra details | `edit_quote()` |
| Delete | Confirms removal of a quotation | `delete_quote()` |

The edit form shows the previously selected features. On submission, the view checks the new choices, recalculates the total, saves the changes, and sets the status back to **Pending** so the admin can review the changed quotation. Delete first shows a confirmation page; the row is deleted only when that form sends a `POST` request.

**Why?** Customers need to correct a quotation or remove one they no longer want. The customer check from Step 5 is repeated for edit, delete, and bill pages.

### Step 10 — Let staff review quotations in admin

`startup/myapp/admin.py` registers `Customer` and `QuoteRequest`. The customer list shows names, email, and phone. It does not show password hashes. The quotation list shows the customer name, service, total, status, and date. Staff can search and filter records, open a quotation to see its selected bill items, and change its status to **Pending**, **Approved**, or **Rejected**.

The saved quotation details are read-only in admin; the admin changes the review status. The customer's dashboard and bill show the current status.

**Why?** The website customer dashboard and Django admin have different jobs. Customers make their own quotations; staff review them. `/admin/` requires a Django admin account, which is separate from a website `Customer` signup.

## Main URLs to demonstrate in class

| URL | What opens |
| --- | --- |
| `/signup/` | Create a customer account |
| `/login/` | Sign in with email and password |
| `/dashboard/` | The signed-in customer's quotations |
| `/quote/` | Service menu |
| `/quote/new/web-development/` | One example of a service feature form |
| `/quote/1/bill/` | Bill for quotation ID 1, if it belongs to this customer |
| `/quote/1/edit/` | Edit that quotation |
| `/quote/1/delete/` | Confirm deletion |
| `/logout/` | Clear the customer session |
| `/admin/` | Staff admin area |

The actual quotation ID may be different from `1`. In templates, `{% url 'quote_bill' quote.id %}` builds the correct link from its URL name and ID.

## One complete classroom example

1. A student signs up with a name, phone, email, and password.
2. Signup saves a `Customer` row and remembers the customer's ID in the session.
3. The student opens the dashboard and clicks **New Quotation**.
4. The student chooses **Web Development**.
5. The student checks **Five-page website** (₹12,000) and **One month maintenance** (₹3,000).
6. The view validates the selections and saves a quotation with a total of **₹15,000** and status **Pending**.
7. The bill shows the two items and the total. The dashboard lists the same quotation.
8. Staff open `/admin/`, review the quotation, and change its status to **Approved**.
9. The student refreshes the dashboard and sees **Approved**. If the student edits the quotation, its status becomes **Pending** again.

## File map

| File | Role in this module |
| --- | --- |
| `startup/myapp/models.py` | Customer and quotation database fields |
| `startup/myapp/migrations/` | Database changes created from the models |
| `startup/myapp/urls.py` | Customer-facing URL paths |
| `startup/myapp/views.py` | Signup, login, session checks, service prices, CRUD, and bill logic |
| `startup/myapp/admin.py` | Staff lists, search, filters, bill items, and review status |
| `startup/templates/signup.html`, `login.html` | Customer account forms |
| `startup/templates/dashboard.html` | Customer quotation list |
| `startup/templates/quote.html` | Service menu |
| `startup/templates/quote_service.html` | Feature selection and edit form |
| `startup/templates/quote_bill.html` | Estimated bill and print button |
| `startup/templates/delete_quote.html` | Delete confirmation |
| `startup/templates/base.html` | Shared page layout and navigation |

