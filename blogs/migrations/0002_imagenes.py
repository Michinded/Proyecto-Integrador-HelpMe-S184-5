# Generated by Django 4.1.7 on 2023-04-16 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Imagenes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('picture', models.ImageField(upload_to='profile_pics/')),
                ('picture_url', models.CharField(blank=True, max_length=255, null=True)),
            ],
        ),
    ]