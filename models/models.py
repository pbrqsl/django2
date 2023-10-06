from django.db import models

# Create your models here.


class Model_template(models.Model):
    brand = models.CharField(max_length=100)

    class Meta:
        abstract = True

class Model1(Model_template):
    property1 = models.PositiveIntegerField()
    property2 = models.CharField(max_length=100)

class Model2(Model_template):
    property1_0 = models.CharField(max_length=30)