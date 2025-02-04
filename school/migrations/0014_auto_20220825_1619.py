# Generated by Django 3.0 on 2022-08-25 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('school', '0013_school_affi'),
    ]

    operations = [
        migrations.AddField(
            model_name='class_subject',
            name='subject_copdf',
            field=models.FileField(blank=True, null=True, upload_to='COpdf/'),
        ),
        migrations.AlterField(
            model_name='assignculturalteacher',
            name='cul_class',
            field=models.CharField(blank=True, choices=[('1', 'Standard 1'), ('2', 'Standard 2'), ('3', 'Standard 3'), ('4', 'Standard 4'), ('5', 'Standard 5'), ('6', 'Standard 6'), ('7', 'Standard 7')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='assignedteacher',
            name='course_class',
            field=models.CharField(blank=True, choices=[('1', 'Standard 1'), ('2', 'Standard 2'), ('3', 'Standard 3'), ('4', 'Standard 4'), ('5', 'Standard 5'), ('6', 'Standard 6'), ('7', 'Standard 7')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='assignsportteacher',
            name='sport_class',
            field=models.CharField(blank=True, choices=[('1', 'Standard 1'), ('2', 'Standard 2'), ('3', 'Standard 3'), ('4', 'Standard 4'), ('5', 'Standard 5'), ('6', 'Standard 6'), ('7', 'Standard 7')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='class_subject',
            name='subject_class',
            field=models.CharField(blank=True, choices=[('1', 'Standard 1'), ('2', 'Standard 2'), ('3', 'Standard 3'), ('4', 'Standard 4'), ('5', 'Standard 5'), ('6', 'Standard 6'), ('7', 'Standard 7')], max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='class_subject',
            name='subject_name',
            field=models.CharField(blank=True, choices=[('English', 'English'), ('Maths', 'Maths'), ('Science', 'Science'), ('Hindi', 'Hindi'), ('Marathi', 'Marathi'), ('History', 'History'), ('Geography', 'Geography'), ('Sanskrit', 'Sanskrit')], max_length=255, null=True),
        ),
    ]
