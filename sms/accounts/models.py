from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Package(models.Model):
    name = models.CharField(max_length=200, null=True)
    price = models.IntegerField(null=True)
    description = models.CharField(max_length=300, null=True)


    def __str__(self):
        return self.name

class Account(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    package = models.ForeignKey(Package, null=True, on_delete=models.CASCADE)
    def __str__(self):
        return self.name