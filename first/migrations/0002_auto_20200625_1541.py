# Generated by Django 3.0.3 on 2020-06-25 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form',
            name='Name',
            field=models.CharField(max_length=50),
        ),
    ]
