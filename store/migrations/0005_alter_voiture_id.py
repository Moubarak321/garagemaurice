# Generated by Django 4.1.6 on 2023-02-25 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0004_remove_voiture_slug_alter_voiture_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='voiture',
            name='id',
            field=models.IntegerField(auto_created=True, primary_key=True, serialize=False),
        ),
    ]
