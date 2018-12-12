from django.db import models
from django.forms import ModelForm

# Create your models here.

class laptops(models.Model):
    lap_id = models.IntegerField( null=True)
    company = models.CharField(max_length=50)
    model_name = models.CharField(max_length=50)
    cost = models.FloatField(max_length=10)
    category =  models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    image_link = models.CharField(max_length=1000, null=True)
    ram = models.CharField(max_length=1000, null=True)
    storage = models.CharField(max_length=1000, null=True)
    weight = models.CharField(max_length=1000, null=True)
    screen_size = models.CharField(max_length=1000, null=True)

    def __str__(self):
        return self.company + ' - ' + self.model_name

class transaction(models.Model):
    username = models.CharField(max_length=1000)
    quantity = models.IntegerField()
    lap_id = models.IntegerField()

    def __str__(self):
        return self.username


class contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    query = models.CharField(max_length=50)

    def __str__(self):
        return self.name


