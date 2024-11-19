from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Galleryvault(models.Model):
    name=models.TextField()
    file=models.FileField()

class Files(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    file=models.ForeignKey(Galleryvault,on_delete=models.CASCADE)
    