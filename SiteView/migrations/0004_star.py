# Generated by Django 4.0.6 on 2022-08-31 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SiteView', '0003_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Star',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.URLField(default='www.google.com', max_length=1024)),
            ],
        ),
    ]