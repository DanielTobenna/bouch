# Generated by Django 3.2 on 2023-01-21 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('greatestinvestapp', '0006_bonus_client_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bonus',
            name='code',
            field=models.CharField(blank=True, max_length=8, null=True, unique=True),
        ),
    ]
