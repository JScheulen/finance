# Generated by Django 5.0.4 on 2024-05-17 03:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Monedas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('moneda', models.CharField(max_length=20)),
                ('descripcion', models.CharField(max_length=255)),
                ('precio', models.FloatField(blank=True)),
            ],
        ),
    ]