# Generated by Django 4.2 on 2023-05-01 22:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('registros', '0009_alter_visita_fecha'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='visita',
            options={'verbose_name_plural': 'registros'},
        ),
        migrations.AlterModelTable(
            name='visita',
            table='registros',
        ),
    ]
