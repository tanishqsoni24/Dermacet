# Generated by Django 4.1.6 on 2023-04-03 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_newsletter'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='product_available_count',
            field=models.IntegerField(default=0),
        ),
    ]
