# Generated by Django 2.1.5 on 2020-04-21 18:14

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0002_auto_20200421_1945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='content',
            field=ckeditor.fields.RichTextField(verbose_name='Contenido'),
        ),
    ]
