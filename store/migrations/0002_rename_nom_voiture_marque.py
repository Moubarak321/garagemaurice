# Generated by Django 4.1.6 on 2023-02-24 14:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='voiture',
            old_name='nom',
            new_name='marque',
        ),
    ]