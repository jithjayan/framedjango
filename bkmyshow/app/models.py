from django.db import models

# Create your models here.

class Movie(models.Model):
    name=models.TextField()
    date=models.DateField()
    frgrnd_img=models.FileField()
    bckgrnd_img=models.FileField()
    lang=models.TextField()
    durtn=models.TextField()
    diamtn=models.TextField()
    type=models.TextField()
    cert=models.TextField()
    about=models.TextField()