# Generated by Django 3.2.3 on 2021-06-01 22:46

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operaciones', '0003_alter_operacion_cantidad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='operacion',
            name='cantidad',
            field=models.IntegerField(
                validators=[
                    django.core.validators.MinValueValidator(1)],
                verbose_name='Cantidad'),
        ),
    ]
