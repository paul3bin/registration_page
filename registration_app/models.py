from django.db import models

# Create your models here.

class RegisterUser(models.Model):
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    email = models.EmailField(max_length=100, unique=True)

    def __str__(self):
        return self.first_name + self.last_name