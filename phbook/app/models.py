from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Phone(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    name=models.TextField()
    email=models.TextField()
    place=models.TextField()
    phone=models.TextField()
    whatsapp=models.TextField()