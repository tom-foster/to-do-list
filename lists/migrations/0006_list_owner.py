# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lists', '0005_list_item_unique_together'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='owner',
<<<<<<< HEAD
            field=models.ForeignKey(blank=True, null=True, to=settings.AUTH_USER_MODEL),
=======
            field=models.ForeignKey(null=True, to=settings.AUTH_USER_MODEL, blank=True),
>>>>>>> d8eddd839eda59aea0ee0445ef4cf82e65328344
        ),
    ]
