# Generated by Django 3.2.12 on 2023-08-28 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_price',
            field=models.IntegerField(),
        ),
    ]
