# Generated by Django 4.1.5 on 2024-04-26 16:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0002_languages_languages_choises'),
    ]

    operations = [
        migrations.AddField(
            model_name='resume',
            name='photo',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='profile'),
            preserve_default=False,
        ),
    ]