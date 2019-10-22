# Generated by Django 2.2.6 on 2019-10-21 16:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('material', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='material',
            name='fecha_mod',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='material',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
