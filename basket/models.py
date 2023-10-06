from django.db import models
from django.views.generic import FormView

# Create your models here.

class Basket(models.Model):
    description = models.CharField(max_length=250, null=True)

class Customer(models.Model):
    username = models.CharField(max_length=60, null=True)
    registration_date = models.DateField(auto_created=True)
    basket = models.ForeignKey(Basket, on_delete=models.CASCADE, null=True, blank=True)