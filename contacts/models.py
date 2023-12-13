from django.db import models
from django.core.validators import EmailValidator
from django.utils import timezone

class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(validators=[EmailValidator()])
    phone = models.CharField(max_length=10, default='')
    created_at = models.DateTimeField(default=timezone.now, editable=False)

    def __str__(self):
        return self.name
