# Generated by Django 4.2.5 on 2023-09-18 07:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='doctor',
            options={'ordering': ['last_name', 'first_name']},
        ),
    ]
