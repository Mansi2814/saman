# Generated by Django 2.2 on 2021-10-22 22:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collection', '0012_men_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='accessory',
            name='desc',
            field=models.CharField(default='Lorem ipsum dolor sit amet consectetur adipisicing elit. Excepturi neque temporibus labore magni voluptate! Deleniti impedit maiores dolor sit corporis placeat perferendis, illum molestias mollitia deserunt nesciunt distinctio', max_length=1000),
        ),
        migrations.AddField(
            model_name='women',
            name='desc',
            field=models.CharField(default='Lorem ipsum dolor sit amet consectetur adipisicing elit. Excepturi neque temporibus labore magni voluptate! Deleniti impedit maiores dolor sit corporis placeat perferendis, illum molestias mollitia deserunt nesciunt distinctio', max_length=1000),
        ),
    ]
