from django.db import models

# Create your models here.
class plants(models.Model):
    p_id=models.TextField()
    name=models.TextField()
    p_type=models.TextField()
    price=models.IntegerField()
    img=models.FileField()
    stock=models.IntegerField()
    disp=models.TextField()