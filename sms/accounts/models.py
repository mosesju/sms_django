from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Account(models.Model):
    PLANS = (
        ('Starter', 'Starter'),
        ('Professional', 'Professional'),
        ('Enterprise', 'Enterprise')
    )
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    plan = models.CharField(max_length=200, null=True, choices=PLANS)
    # group =
    # texts = 
    def __str__(self):
        return self.name

class Plan(models.Model):
    PLANS = (
        ('Starter', 'Starter'),
        ('Professional', 'Professional'),
        ('Enterprise', 'Enterprise')
    )
    plans = models.CharField(max_length=200, null=True, choices=PLANS)
    price = models.IntegerField(null=True)
