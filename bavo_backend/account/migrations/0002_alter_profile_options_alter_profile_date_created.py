# Generated by Django 4.2.4 on 2023-09-21 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='profile',
            options={},
        ),
        migrations.AlterField(
            model_name='profile',
            name='date_created',
            field=models.DateField(auto_created=True, auto_now=True),
        ),
    ]
