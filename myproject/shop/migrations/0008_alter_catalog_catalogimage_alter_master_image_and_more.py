# Generated by Django 5.1.2 on 2024-11-29 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0007_remove_glavnyiimage_galleryimage_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='catalog',
            name='catalogImage',
            field=models.ImageField(blank=True, null=True, upload_to='catalog_image'),
        ),
        migrations.AlterField(
            model_name='master',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='master_image'),
        ),
        migrations.AlterField(
            model_name='services',
            name='servicesImage',
            field=models.ImageField(blank=True, null=True, upload_to='services_image'),
        ),
        migrations.AlterField(
            model_name='servicesprofileimage',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='services_image'),
        ),
        migrations.AlterField(
            model_name='сompanyprofile',
            name='company_image',
            field=models.ImageField(blank=True, null=True, upload_to='company_image'),
        ),
        migrations.AlterField(
            model_name='сompanyprofileimage',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='company_image'),
        ),
    ]