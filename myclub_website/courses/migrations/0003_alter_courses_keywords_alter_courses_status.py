# Generated by Django 4.0.3 on 2022-06-11 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_remove_category_description_remove_category_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses',
            name='keywords',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='courses',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
