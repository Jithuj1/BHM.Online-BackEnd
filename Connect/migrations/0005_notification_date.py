# Generated by Django 4.0.6 on 2023-02-23 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Connect', '0004_notification'),
    ]

    operations = [
        migrations.AddField(
            model_name='notification',
            name='date',
            field=models.DateField(auto_now=True, null=True),
        ),
    ]
