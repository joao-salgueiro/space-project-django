# Generated by Django 5.1.7 on 2025-03-20 20:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0002_photograph_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='photograph',
            name='publicated',
            field=models.BooleanField(default=False),
        ),
    ]
