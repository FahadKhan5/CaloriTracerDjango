# Generated by Django 4.2.5 on 2023-10-14 14:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='food',
            old_name='carb',
            new_name='carbs',
        ),
    ]
