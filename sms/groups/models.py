from django.db import models
from accounts.models import Account
# Create your models here.
class Group(models.Model):
    account = models.ForeignKey(Account, null=True, on_delete=models.CASCADE)
    group_name = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=200, null=True)
    def __str__(self):
        return self.group_name

class Contact(models.Model):
    group = models.ForeignKey(Group, null=True, on_delete=models.CASCADE)
    phone = models.CharField(max_length=200, null=True)