# Generated by Django 3.2.3 on 2021-06-02 00:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tareaSorpresa', '0004_alter_nota_descripcion'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nota',
            name='fecha_finalizacion',
            field=models.DateField(verbose_name='Fecha finalizacion:'),
        ),
    ]
