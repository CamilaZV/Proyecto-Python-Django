# Generated by Django 5.0 on 2024-01-03 13:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Academica', '0002_rename_apellidomaterno_estudiante_apellido_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='estudiante',
            name='vigencia',
        ),
    ]