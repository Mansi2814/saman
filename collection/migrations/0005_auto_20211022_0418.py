# Generated by Django 2.2 on 2021-10-21 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0004_auto_20211022_0416'),
    ]

    operations = [
        migrations.AlterField(
            model_name='men',
            name='product_img',
            field=models.ImageField(null=True, upload_to='collection/static/img'),
        ),
    ]
