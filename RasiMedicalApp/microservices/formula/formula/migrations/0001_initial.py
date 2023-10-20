# Generated by Django 4.2.6 on 2023-10-08 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Formula',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dose', models.CharField(max_length=255)),
                ('frequency', models.CharField(max_length=255)),
                ('unity', models.CharField(max_length=255)),
                ('medicamentId', models.IntegerField()),
                ('presentation', models.CharField(max_length=255)),
            ],
        ),
    ]