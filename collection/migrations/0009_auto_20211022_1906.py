# Generated by Django 2.2 on 2021-10-22 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0008_men_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='men',
            name='featured',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='men',
            name='latest',
            field=models.BooleanField(default=False),
        ),
    ]
