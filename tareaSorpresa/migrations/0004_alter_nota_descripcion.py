# Generated by Django 3.2.3 on 2021-06-01 23:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tareaSorpresa', '0003_auto_20210601_1919'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nota',
            name='descripcion',
            field=models.TextField(verbose_name='Descripcion:'),
        ),
    ]