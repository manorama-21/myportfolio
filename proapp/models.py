from django.db import models

class promodel(models.Model):
    name = models.CharField(max_length=250)
    email = models.EmailField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.CharField(max_length=255)
# Create your models here.
