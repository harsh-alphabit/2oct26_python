from django.db import models

# Create your models here.
class user_signup(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField()
    password=models.CharField(max_length=12)
    mobile=models.BigIntegerField()
    address=models.TextField()

    def __str__(self) -> str:
        return self.name
