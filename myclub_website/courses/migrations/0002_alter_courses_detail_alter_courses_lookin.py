# Generated by Django 4.0.3 on 2022-05-21 11:25

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='detail',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
        migrations.AlterField(
            model_name='courses',
            name='lookin',
            field=ckeditor_uploader.fields.RichTextUploadingField(),
        ),
    ]
