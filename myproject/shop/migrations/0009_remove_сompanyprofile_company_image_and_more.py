# Generated by Django 5.1.2 on 2024-11-29 09:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_alter_catalog_catalogimage_alter_master_image_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='сompanyprofile',
            name='company_image',
        ),
        migrations.DeleteModel(
            name='ServicesProfileImage',
        ),
    ]
