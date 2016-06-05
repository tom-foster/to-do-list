from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse

# Create your models here.
#List class needs to be declared prior to it's assigning in Item
class List(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, blank=True, null=True)

    def get_absolute_url(self):
        return reverse('view_list', args=[self.id])

<<<<<<< HEAD
    @staticmethod
    def create_new(first_item_text, owner=None):
        list_ = List.objects.create(owner=owner)
        Item.objects.create(text=first_item_text, list=list_)
        return list_

=======
>>>>>>> d8eddd839eda59aea0ee0445ef4cf82e65328344
    @property
    def name(self):
        return self.item_set.first().text

<<<<<<< HEAD

=======
>>>>>>> d8eddd839eda59aea0ee0445ef4cf82e65328344

class Item(models.Model):
    text = models.TextField(default='')
    list = models.ForeignKey(List, default=None)

    class Meta:
        ordering = ('id',)
        unique_together = ('list', 'text')

    def __str__(self):
        return self.text
