# Generated by Django 5.1.2 on 2024-11-29 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_master_description_en_master_description_ky_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='glavnyiimage',
            name='galleryImage',
        ),
        migrations.AddField(
            model_name='glavnyiimage',
            name='description',
            field=models.TextField(default=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='glavnyiimage',
            name='description_en',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='glavnyiimage',
            name='description_ky',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='glavnyiimage',
            name='description_ru',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='glavnyiimage',
            name='work_name_en',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='glavnyiimage',
            name='work_name_ky',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='glavnyiimage',
            name='work_name_ru',
            field=models.CharField(blank=True, max_length=32, null=True),
        ),
    ]
