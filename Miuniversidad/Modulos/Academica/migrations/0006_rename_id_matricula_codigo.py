# Generated by Django 5.0 on 2024-01-05 22:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Academica', '0005_alter_estudiante_carrera'),
    ]

    operations = [
        migrations.RenameField(
            model_name='matricula',
            old_name='id',
            new_name='codigo',
        ),
    ]
