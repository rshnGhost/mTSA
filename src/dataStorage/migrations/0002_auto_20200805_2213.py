# Generated by Django 2.2.1 on 2020-08-05 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataStorage', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cache',
            name='tag',
            field=models.CharField(max_length=140, null=True, unique=True),
        ),
    ]
