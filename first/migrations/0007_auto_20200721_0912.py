# Generated by Django 3.0.8 on 2020-07-21 03:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('first', '0006_auto_20200713_0928'),
    ]

    operations = [
        migrations.CreateModel(
            name='GalleryImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('HoverTitle', models.CharField(max_length=255)),
                ('PicTitle', models.CharField(max_length=255)),
                ('Image', models.ImageField(upload_to='gallery_pics/')),
            ],
        ),
        migrations.AlterField(
            model_name='feedback',
            name='Name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='form',
            name='Country',
            field=models.CharField(default=0, max_length=255),
        ),
        migrations.AlterField(
            model_name='form',
            name='Email',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='form',
            name='Name',
            field=models.CharField(max_length=255),
        ),
    ]
