from django.db import models


# Create your models here.

class Tovar(models.Model):
    image = models.ImageField(blank=True, null=True)
    title = models.CharField(max_length=255)
    price = models.FloatField()
    quantity = models.IntegerField()
    description = models.TextField()
    created_date = models.DateField(auto_now=True)
    modified_date = models.DateField(auto_now_add=True)
