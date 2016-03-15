from django.db import models

# Create your models here.
#List class needs to be declared prior to it's assigning in Item
class List(models.Model):
    pass

class Item(models.Model):
    text = models.TextField(default='')
    list = models.ForeignKey(List, default=None)
