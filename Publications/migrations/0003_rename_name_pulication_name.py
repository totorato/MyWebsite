# Generated by Django 4.1 on 2022-08-27 08:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Publications', '0002_alter_pulication_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pulication',
            old_name='Name',
            new_name='name',
        ),
    ]