# Generated by Django 4.1.5 on 2023-01-09 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Doctor', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctors',
            name='status',
            field=models.BooleanField(default=False),
        ),
    ]
