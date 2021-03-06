# Generated by Django 3.2.3 on 2021-06-02 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipos', '0004_alter_equipo_disponibilidad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='equipo',
            name='disponibilidad',
            field=models.CharField(
                choices=[
                    ('Disponible',
                     'D'),
                    ('No disponible',
                     'ND')],
                max_length=20,
                verbose_name='Disponibilidad'),
        ),
    ]
