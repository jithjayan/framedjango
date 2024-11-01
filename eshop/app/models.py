from django.db import models

# Create your models here.
class product(models.Model):
    pro_id=models.IntegerField()
    name=models.TextField()
    price=models.IntegerField()
    offer_price=models.IntegerField()
    img=models.FileField()
    disp=models.TextField()
    