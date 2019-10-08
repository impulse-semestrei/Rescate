# Generated by Django 2.2.6 on 2019-10-08 15:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('material', '0004_remove_material_cantidad'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inventario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Inventario_Material',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cantidad', models.IntegerField()),
                ('inventario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventario.Inventario')),
                ('material', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='material.Material')),
            ],
        ),
        migrations.AddField(
            model_name='inventario',
            name='materiales',
            field=models.ManyToManyField(through='inventario.Inventario_Material', to='material.Material'),
        ),
    ]
