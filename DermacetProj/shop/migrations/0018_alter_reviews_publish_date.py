# Generated by Django 4.1.6 on 2023-05-24 10:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0017_alter_reviews_publish_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='publish_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 5, 24, 15, 31, 42, 775435)),
        ),
    ]