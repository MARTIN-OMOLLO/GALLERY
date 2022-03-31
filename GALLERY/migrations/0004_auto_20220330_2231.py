# Generated by Django 3.2.7 on 2022-03-30 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GALLERY', '0003_alter_photos_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='photos',
            name='location',
            field=models.ManyToManyField(to='GALLERY.Location'),
        ),
    ]
