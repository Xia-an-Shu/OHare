# Generated by Django 4.2.6 on 2023-10-08 22:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('formula', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='formula',
            old_name='medicamentId',
            new_name='medicationId',
        ),
    ]