# Generated by Django 4.0.6 on 2023-01-18 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Doctor', '0010_alter_doctors_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctors',
            name='image',
            field=models.FileField(null=True, upload_to='Image/Doctors/'),
        ),
    ]
