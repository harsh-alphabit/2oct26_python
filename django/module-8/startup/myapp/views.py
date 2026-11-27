from django.shortcuts import render, redirect, get_object_or_404
from .models import QuoteRequest, Customer
from .forms import ContactUs, SubscriberForm
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.hashers import make_password, check_password
from django.core.exceptions import ValidationError

# Create your views here.

# Sample prices for classroom practice. Each service has its own selectable work.
SERVICES = {
    'cyber-security': {'name': 'Cyber Security', 'features': [
        ('audit', 'Security audit', 5000),
        ('malware', 'Malware removal', 3500),
        ('monitoring', 'One month monitoring', 2500),
    ]},
    'data-analytics': {'name': 'Data Analytics', 'features': [
        ('cleaning', 'Data cleaning', 3000),
        ('dashboard', 'Analytics dashboard', 7000),
        ('report', 'Business report', 4000),
    ]},
    'web-development': {'name': 'Web Development', 'features': [
        ('website', 'Five-page website', 12000),
        ('store', 'Online store', 15000),
        ('maintenance', 'One month maintenance', 3000),
    ]},
    'apps-development': {'name': 'Apps Development', 'features': [
        ('android', 'Android app', 20000),
        ('ios', 'iPhone app', 22000),
        ('notifications', 'Push notifications', 5000),
    ]},
    'seo-optimization': {'name': 'SEO Optimization', 'features': [
        ('keywords', 'Keyword research', 2500),
        ('onpage', 'On-page SEO', 4500),
        ('monthly', 'One month SEO report', 2000),
    ]},
}

def index(request):
    # render() loads the HTML template, fills it with any supplied data, and returns the page.
    return render(request, 'index.html')

def about(request):
    # render() loads the HTML template, fills it with any supplied data, and returns the page.
    return render(request, 'about.html')

def contact(request):
    # ContactUs is our ModelForm class. Calling it without data makes an empty form.
    contactusform = ContactUs()
    if request.method == 'POST':
        # Pass the submitted form fields to our ModelForm so Django can check them.
        contactusform=ContactUs(request.POST)
        # is_valid() checks the form data and returns True if there are no validation errors.
        if contactusform.is_valid():
            # ModelForm save() creates a database record from the valid form data.
            contactusform.save()
            print("message got successfully")
            # redirect() tells the browser to open another URL; '/' means the home page.
            return redirect('contact')

    # render() loads the HTML template, fills it with any supplied data, and returns the page.
    return render(request, 'contact.html', {'form': contactusform})

def feature(request):
    # render() loads the HTML template, fills it with any supplied data, and returns the page.
    return render(request, 'feature.html')

def quote(request):
    # session.get() reads the saved ID. filter() finds matching rows; first() returns one or None.
    customer = Customer.objects.filter(id=request.session.get('customer_id')).first()
    if not customer:
        # redirect() tells the browser to open another URL; '/' means the home page.
        return redirect('login')
    # render() loads the HTML template, fills it with any supplied data, and returns the page.
    return render(request, 'quote.html', {'services': SERVICES})


def create_quote(request, service):
    # Session get() reads the saved customer ID; it returns None if the key is missing.
    customer_id = request.session.get('customer_id')
    # filter() finds matching database rows. first() returns the first row, or None.
    customer = Customer.objects.filter(id=customer_id).first()
    if not customer:
        # redirect() sends the browser to the URL named 'login'.
        return redirect('login')
    # Dictionary get() reads this service's details, or returns None if it is missing.
    service_info = SERVICES.get(service)
    if not service_info:
        # Open the service selection page using its URL name.
        return redirect('quote')

    error = ''
    selected = []
    message = ''
    if request.method == 'POST':
        # getlist() reads all checked values named 'features' into a list.
        selected = request.POST.getlist('features')
        # POST get() reads the message, or '' if missing. strip() removes spaces at both ends.
        message = request.POST.get('message', '').strip()

        allowed = []
        total = 0
        for code, label, price in service_info['features']:
            # append() adds one feature code to the end of the list.
            allowed.append(code)
            if code in selected:
                total += price

        if not selected:
            error = 'Choose at least one feature.'

        seen = []
        for code in selected:
            if code not in allowed:
                error = 'Please choose features from the list.'
                break
            if code in seen:
                error = 'Please choose each feature only once.'
                break
            # Remember this code so we can detect it if it appears again.
            seen.append(code)

        if not error:
            # create() makes a database row, saves it, and returns the new quote object.
            new_quote = QuoteRequest.objects.create(
                customer=customer,
                name=customer.first_name + ' ' + customer.last_name,
                email=customer.email,
                service=service_info['name'],
                # join() combines the codes into text, for example: 'website,maintenance'.
                features=','.join(selected),
                total_price=total,
                message=message,
            )
            # Open the bill URL with the new quote's ID.
            return redirect('quote_bill', id=new_quote.id)

    # render() builds the HTML page using the template and the data below.
    return render(request, 'quote_service.html', {
        'service': service_info, 'error': error, 'selected': selected,
        'message': message, 'editing': False,
    })


def edit_quote(request, id):
    # Session get() reads the saved customer ID; it returns None if the key is missing.
    customer_id = request.session.get('customer_id')
    # filter() finds matching database rows. first() returns the first row, or None.
    customer = Customer.objects.filter(id=customer_id).first()
    if not customer:
        # redirect() sends the browser to the URL named 'login'.
        return redirect('login')

    # Get this customer's quote. If it does not exist, show a 404 (not found) page.
    quote_request = get_object_or_404(QuoteRequest, id=id, customer=customer)
    service_info = None
    # values() gives the service details stored in the dictionary, without its keys.
    for service in SERVICES.values():
        if service['name'] == quote_request.service:
            service_info = service
            break
    if not service_info:
        # Open the URL named 'dashboard'.
        return redirect('dashboard')

    error = ''
    # split(',') turns 'website,maintenance' into ['website', 'maintenance'].
    selected = quote_request.features.split(',')
    message = quote_request.message
    if request.method == 'POST':
        # getlist() reads all checked values named 'features' into a list.
        selected = request.POST.getlist('features')
        # POST get() reads the message, or '' if missing. strip() removes spaces at both ends.
        message = request.POST.get('message', '').strip()

        allowed = []
        total = 0
        for code, label, price in service_info['features']:
            # append() adds one feature code to the end of the list.
            allowed.append(code)
            if code in selected:
                total += price

        if not selected:
            error = 'Choose at least one feature.'

        seen = []
        for code in selected:
            if code not in allowed:
                error = 'Please choose features from the list.'
                break
            if code in seen:
                error = 'Please choose each feature only once.'
                break
            # Remember this code so we can detect it if it appears again.
            seen.append(code)

        if not error:
            # join() turns the selected codes into comma-separated text for storage.
            quote_request.features = ','.join(selected)
            quote_request.total_price = total
            quote_request.message = message
            # If the customer edits a quote, the admin must review the new details again.
            # Even an Approved or Rejected quote goes back to Pending when this edit is saved.
            quote_request.status = 'Pending'
            # save() writes the changed quote details to the database.
            quote_request.save()
            # Open the bill URL with this quote's ID.
            return redirect('quote_bill', id=quote_request.id)

    # render() builds the HTML page using the template and the data below.
    return render(request, 'quote_service.html', {
        'service': service_info, 'error': error, 'selected': selected,
        'message': message, 'editing': True,
    })


def quote_bill(request, id):
    # Session get() reads the saved customer ID; it returns None if the key is missing.
    customer_id = request.session.get('customer_id')
    # filter() finds matching database rows. first() returns the first row, or None.
    customer = Customer.objects.filter(id=customer_id).first()
    if not customer:
        # redirect() sends the browser to the URL named 'login'.
        return redirect('login')
    # Get this customer's quote. If it does not exist, show a 404 (not found) page.
    quote_request = get_object_or_404(QuoteRequest, id=id, customer=customer)
    # split(',') turns 'website,maintenance' into ['website', 'maintenance'].
    selected = quote_request.features.split(',')
    items = []
    # values() gives the service details stored in the dictionary, without its keys.
    for service in SERVICES.values():
        if service['name'] == quote_request.service:
            for code, label, price in service['features']:
                if code in selected:
                    # append() adds one (feature name, price) pair to the bill's list.
                    items.append((label, price))
            break
    # render() builds the bill page with the quote and its selected items.
    return render(request, 'quote_bill.html', {'quote_request': quote_request, 'items': items})


def delete_quote(request, id):
    # session.get() reads the saved ID. filter() finds matching rows; first() returns one or None.
    customer = Customer.objects.filter(id=request.session.get('customer_id')).first()
    if not customer:
        # redirect() tells the browser to open another URL; '/' means the home page.
        return redirect('login')

    # get_object_or_404() gets this customer's quote, or shows a 404 page if no match exists.
    quote_request = get_object_or_404(QuoteRequest, id=id, customer=customer)
    if request.method == 'POST':
        # delete() removes this quote from the database.
        quote_request.delete()
        # redirect() tells the browser to open another URL; '/' means the home page.
        return redirect('dashboard')

    # render() loads the HTML template, fills it with any supplied data, and returns the page.
    return render(request, 'delete_quote.html', {'quote_request': quote_request})

def service(request):
    # render() loads the HTML template, fills it with any supplied data, and returns the page.
    return render(request,'service.html')

def team(request):
    # render() loads the HTML template, fills it with any supplied data, and returns the page.
    return render(request,'team.html')

def testimonial(request):
    # render() loads the HTML template, fills it with any supplied data, and returns the page.
    return render(request,'testimonial.html')


def search(request):
    # GET.get() reads a URL query value; '' is used when q is missing.
    q = request.GET.get('q', '').strip()
    #'q' is the input’s name. Django looks for q in a URL such as /search/?q=Cyber.
    #'' is the default: an empty string used when the URL has no q.
    results = []

    if q:
        for value, label in QuoteRequest.services:
            #quoterequest.services= services is the list you already wrote inside the QuoteRequest model
            if q.lower() in label.lower():
                results.append(label)

    # render() loads the HTML template, fills it with any supplied data, and returns the page.
    return render(request, 'search.html', {'q': q, 'results': results})


def subscribe(request):
    if request.method == 'POST':
        # SubscriberForm is our ModelForm class; request.POST supplies the submitted fields.
        form = SubscriberForm(request.POST)
        # is_valid() checks the form's field rules, including email format and uniqueness here.
        if form.is_valid():
            # ModelForm save() saves the valid subscriber details in the database.
            form.save()
            # messages.success() stores a temporary success message for the template to display.
            messages.success(request, 'Thank you for subscribing.')
        else:
            # messages.error() stores a temporary error message for the template to display.
            messages.error(request, 'Enter a valid email address that is not already subscribed.')

    # redirect() tells the browser to open another URL; '/' means the home page.
    return redirect('/')


def signup(request):
    # session.get() reads the saved customer ID; None means this key is missing.
    if request.session.get('customer_id'):
        # redirect() tells the browser to open another URL; '/' means the home page.
        return redirect('dashboard')

    error = ''
    if request.method == 'POST':
        # POST.get() reads one submitted field, or the default '' if it is missing.
        first_name = request.POST.get('first_name', '').strip()
        last_name = request.POST.get('last_name', '').strip()
        phone_number = request.POST.get('phone_number', '').strip()
        # POST.get() reads the email; Python strip() trims its ends and lower() makes it lowercase.
        email = request.POST.get('email', '').strip().lower()
        # POST.get() reads the submitted password, or '' if no password field was sent.
        password = request.POST.get('password', '')

        if not all([first_name, last_name, phone_number, email, password]):
            error = 'Please fill in all fields.'
        elif not phone_number.isdigit():
            error = 'Phone number must contain digits only.'
        # filter() finds matches ignoring letter case (__iexact); exists() returns True if any match exists.
        elif Customer.objects.filter(email__iexact=email).exists():
            error = 'This email is already registered.'
        else:
            # Create a Customer object in memory. It is not saved in the database yet.
            customer = Customer(first_name=first_name, last_name=last_name,
                                phone_number=phone_number, email=email,
                                # make_password() turns the password into a one-way hash for storage, not readable text.
                                password=make_password(password))
            try:
                # full_clean() checks model field rules and uniqueness; it does not save the customer.
                customer.full_clean()
            # ValidationError is Django's exception for invalid data; handle it by showing an error.
            except ValidationError:
                error = 'Please enter valid details.'
            else:
                # Model save() writes this customer to the database.
                customer.save()
                # cycle_key() gives the session a new ID while keeping its data, helping protect the login.
                request.session.cycle_key()
                request.session['customer_id'] = customer.id
                #Session key: Django generates this automatically. It identifies the visitor’s session. 
                # cycle_key() replaces it with a new one.
                #'customer_id': This is a name we chose for a value inside the session. Django does not know that we want to remember a customer, so we must store it
                
                # redirect() tells the browser to open another URL; '/' means the home page.
                return redirect('dashboard')

    # render() loads the HTML template, fills it with any supplied data, and returns the page.
    return render(request, 'signup.html', {'error': error})


def user_login(request):
    # session.get() reads the saved customer ID; None means this key is missing.
    if request.session.get('customer_id'):
        # redirect() tells the browser to open another URL; '/' means the home page.
        return redirect('dashboard')

    error = ''
    if request.method == 'POST':
        # POST.get() reads the email; Python strip() trims its ends and lower() makes it lowercase.
        email = request.POST.get('email', '').strip().lower()
        # POST.get() reads the submitted password, or '' if no password field was sent.
        password = request.POST.get('password', '')
        # Find the email ignoring letter case. first() returns a customer, or None if not found.
        customer = Customer.objects.filter(email__iexact=email).first()
        # check_password() compares the typed password with the stored hash and returns True if it matches.
        if customer and check_password(password, customer.password):
            # cycle_key() gives the session a new ID while keeping its data, helping protect the login.
            request.session.cycle_key()
            request.session['customer_id'] = customer.id
            # redirect() tells the browser to open another URL; '/' means the home page.
            return redirect('dashboard')
        error = 'Incorrect email or password.'

    # render() loads the HTML template, fills it with any supplied data, and returns the page.
    return render(request, 'login.html', {'error': error})


def dashboard(request):
    # session.get() reads the saved ID. filter() finds matching rows; first() returns one or None.
    customer = Customer.objects.filter(id=request.session.get('customer_id')).first()
    if not customer:
        # redirect() tells the browser to open another URL; '/' means the home page.
        return redirect('login')
    # filter() selects this customer's quotes; order_by('-id') puts the highest IDs first.
    # Fetch saved statuses too, so reloading the dashboard shows the admin's latest changes.
    quotes = QuoteRequest.objects.filter(customer=customer).order_by('-id')
    # render() loads the HTML template, fills it with any supplied data, and returns the page.
    return render(request, 'dashboard.html', {'customer': customer, 'quotes': quotes})


def user_logout(request):
    # Django logout() clears the whole session, including our saved customer_id.
    logout(request)
    # redirect() tells the browser to open another URL; '/' means the home page.
    return redirect('/')
