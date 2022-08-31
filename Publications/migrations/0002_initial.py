# Generated by Django 4.0.6 on 2022-08-31 13:12

from django.db import migrations, models
import imagekit.models.fields
import mdeditor.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Publications', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='the name of the publication or project.', max_length=1024)),
                ('teaser', imagekit.models.fields.ProcessedImageField(default='avatar2/matthew.png', upload_to='avatar2', verbose_name='teaser')),
                ('introduction', mdeditor.fields.MDTextField()),
                ('addinfo', models.CharField(default='', help_text='oral? best paper?', max_length=1024)),
            ],
        ),
    ]