# Generated by Django 4.1.2 on 2024-02-24 21:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='created_at',
            new_name='created_at_time',
        ),
    ]
