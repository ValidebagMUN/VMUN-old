# Generated by Django 4.1.5 on 2023-01-17 05:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('committee', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='committee',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
