# Generated by Django 4.0.6 on 2023-01-18 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Hospital', '0003_alter_hospitals_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospitals',
            name='image',
            field=models.FileField(null=True, upload_to='Image/Hospital/'),
        ),
    ]