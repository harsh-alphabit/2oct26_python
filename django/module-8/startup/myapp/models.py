from django.db import models
from django.utils import timezone

# Create your models here.

class ContactForm(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=200)
    message = models.TextField()
    created_at = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return f"{self.name} - {self.subject}"


class QuoteRequest(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    ]
    services = [
        ('Cyber Security', 'Cyber Security'), # value saved in database, text shown to the user
        ('Data Analytics', 'Data Analytics'),
        ('Web Development', 'Web Development'),
        ('Apps Development', 'Apps Development'),
        ('SEO Optimization', 'SEO Optimization'),
    ]

    customer = models.ForeignKey('Customer', on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    service = models.CharField(max_length=100, choices=services)
    message = models.TextField(blank=True)
    # Feature codes are saved as a comma-separated list, for example: audit,monitoring.
    features = models.CharField(max_length=200, blank=True)
    total_price = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')

    def __str__(self):
        return f"{self.name} - {self.service}"


class Subscriber(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email


class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=128)

    def __str__(self):
        return self.email
