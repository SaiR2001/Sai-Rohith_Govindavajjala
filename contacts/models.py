# contacts/models.py
from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=10, default='')  # You can set a default value here

    def __str__(self):
        return self.name

