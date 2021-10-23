# Generated by Django 2.2 on 2021-10-21 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Men',
            fields=[
                ('product_id', models.CharField(max_length=20, primary_key=True, serialize=False)),
                ('category', models.CharField(max_length=122)),
                ('name', models.CharField(max_length=50)),
                ('Price', models.CharField(max_length=100)),
                ('product_img', models.ImageField(null=True, upload_to='collection/images')),
            ],
        ),
    ]