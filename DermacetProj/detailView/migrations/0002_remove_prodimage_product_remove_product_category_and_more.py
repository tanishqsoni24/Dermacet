# Generated by Django 4.1.7 on 2023-03-25 10:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('detailView', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='prodimage',
            name='product',
        ),
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='ProdImage',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
    ]
