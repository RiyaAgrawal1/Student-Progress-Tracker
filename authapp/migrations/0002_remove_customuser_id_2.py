# Generated by Django 3.0 on 2022-07-28 19:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='id_2',
        ),
    ]
