# Generated by Django 3.1 on 2020-08-31 05:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]