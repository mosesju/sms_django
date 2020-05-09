from django.db import models

# Create your models here.
class Group(models.Model):
    # account = d
    group_name = models.CharField(max_length=200, null=True)
    description = models.CharField(max_length=200, null=True)
    def __str__(self):
        return self.group_name

class Contact(models.Model):
    group = models.CharField(max_length=200, null=True)
    phone = models.CharField(max_length=200, null=True)