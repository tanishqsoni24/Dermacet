# Generated by Django 4.1.6 on 2023-06-01 18:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0019_alter_reviews_publish_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='publish_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 6, 2, 0, 10, 44, 262517)),
        ),
    ]
