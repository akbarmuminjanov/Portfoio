# Generated by Django 4.1.5 on 2024-04-26 16:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='languages',
            name='languages_choises',
            field=models.CharField(choices=[('nt', 'native'), ('fl', 'fluent')], default=django.utils.timezone.now, max_length=60),
            preserve_default=False,
        ),
    ]
