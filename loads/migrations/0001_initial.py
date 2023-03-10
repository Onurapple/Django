# Generated by Django 4.1.7 on 2023-03-13 18:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Loads',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('load_name', models.CharField(max_length=30)),
                ('load_type', models.CharField(choices=[('K', 'Complate'), ('P', 'Parsial'), ('KP', 'Copm-Pars')], default='K', max_length=2)),
                ('weight', models.IntegerField(blank=True, null=True)),
                ('register_date', models.DateTimeField(auto_now_add=True)),
                ('update_date', models.DateTimeField(auto_now=True)),
                ('load_pic', models.ImageField(blank=True, upload_to='profile_pics')),
            ],
            options={
                'verbose_name_plural': 'Yükler',
            },
        ),
        migrations.CreateModel(
            name='Warehouse',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('warehouse_name', models.CharField(max_length=30)),
                ('warehouse_location', models.CharField(choices=[('IST', 'Istanbul'), ('ANK', 'Ankara'), ('IZM', 'Izmir')], default='IST', max_length=3)),
                ('included_loads', models.ManyToManyField(to='loads.loads')),
            ],
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner_name', models.CharField(max_length=30)),
                ('owners_load', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='loads.loads')),
            ],
        ),
    ]
