# Generated by Django 2.2 on 2021-10-22 23:41

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0013_auto_20211023_0335'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('product_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('quantity', models.IntegerField(default=1)),
                ('ordered_on', models.DateField(default=datetime.date.today)),
                ('deliverd', models.BooleanField(default=False)),
                ('delivered_on', models.DateField(default='18/10/2021')),
                ('expected_delivery', models.DateField(default='30/10/2021')),
                ('mop', models.CharField(default='COD', max_length=20)),
            ],
        ),
    ]
