# Generated by Django 3.0 on 2022-08-26 08:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0018_auto_20220826_0653'),
    ]

    operations = [
        migrations.AddField(
            model_name='cultural',
            name='cultural_level',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
