# Generated by Django 4.0.5 on 2022-06-14 06:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='zipcode',
        ),
    ]
