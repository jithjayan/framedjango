from django.db import models

# Create your models here.
class Galleryvault(models.Model):
    name=models.TextField()
    file=models.FileField()