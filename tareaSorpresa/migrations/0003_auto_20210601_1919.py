# Generated by Django 3.2.3 on 2021-06-01 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tareaSorpresa', '0002_nota_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nota',
            name='estado',
            field=models.BooleanField(default=0, verbose_name='Estado:'),
        ),
        migrations.AlterField(
            model_name='nota',
            name='fecha_finalizacion',
            field=models.DateTimeField(verbose_name='Fecha finalizacion:'),
        ),
    ]
