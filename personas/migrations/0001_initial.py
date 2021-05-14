# Generated by Django 3.1.7 on 2021-03-30 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombres', models.CharField(max_length=200)),
                ('apellidos', models.CharField(max_length=200)),
                ('ciudad', models.CharField(max_length=200)),
                ('edad', models.IntegerField()),
                ('fecha_nacimiento', models.DateField(null=True)),
                ('genero', models.IntegerField(choices=[(1, 'Masculino'), (0, 'Femenino'), (-1, 'Otro')], default=-1)),
                ('email', models.CharField(max_length=100)),
            ],
        ),
    ]
