# Generated by Django 4.2.7 on 2023-11-15 19:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appmanager', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='rol',
            options={'ordering': ['rol_cod']},
        ),
    ]