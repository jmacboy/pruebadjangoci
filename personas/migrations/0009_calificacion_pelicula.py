# Generated by Django 3.1.7 on 2021-04-23 18:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('personas', '0008_auto_20210423_1331'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pelicula',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('director', models.CharField(max_length=200)),
                ('sinopsis', models.CharField(max_length=500)),
                ('anio', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Calificacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valor', models.IntegerField()),
                ('pelicula', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='calificaciones', to='personas.pelicula')),
                ('persona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='calificaciones', to='personas.persona')),
            ],
        ),
    ]
