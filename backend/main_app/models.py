from django.db import models

# Create your models here.

class RegisterModel(models.Model):
    name = models.CharField(max_length=255)
    mail = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    #admin can see type of model with _str_ function
    def __str__(self):
        return self.name
    class Meta:
        ordering = ['name']
    