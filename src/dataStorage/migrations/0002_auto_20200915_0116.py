# Generated by Django 2.2.1 on 2020-09-14 19:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dataStorage', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='phonebench',
            old_name='ddd',
            new_name='gpu',
        ),
        migrations.AddField(
            model_name='phonebench',
            name='mem',
            field=models.IntegerField(null=True),
        ),
    ]
