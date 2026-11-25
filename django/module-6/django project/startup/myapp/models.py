from django.db import models

# Create your models here.

class ContactForm(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.subject}"


class QuoteRequest(models.Model):
    services = [
        ('Cyber Security', 'Cyber Security'), # value saved in database, text shown to the user
        ('Data Analytics', 'Data Analytics'),
        ('Web Development', 'Web Development'),
        ('Apps Development', 'Apps Development'),
        ('SEO Optimization', 'SEO Optimization'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    service = models.CharField(max_length=100, choices=services)
    message = models.TextField()

    def __str__(self):
        return f"{self.name} - {self.service}"


class Subscriber(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.email
