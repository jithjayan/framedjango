from django.db import models

# Create your models here.
class Course(models.Model):
    img=models.FileField()
    name=models.TextField()
    details=models.TextField()
    durt=models.TextField()
    fees=models.IntegerField()

class enqry(models.Model):
    name=models.TextField()
    email=models.EmailField()
    phnum=models.IntegerField()
    msg=models.TextField()
    