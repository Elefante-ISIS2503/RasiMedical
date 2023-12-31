# Generated by Django 3.2.6 on 2023-09-26 23:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('cedula', models.CharField(max_length=10)),
                ('correo', models.CharField(max_length=50)),
                ('fechaNacimiento', models.DateField()),
                ('rol', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Profesional',
            fields=[
                ('usuario_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='profesionales.usuario')),
                ('especialidad', models.CharField(max_length=50)),
            ],
            bases=('profesionales.usuario',),
        ),
    ]
