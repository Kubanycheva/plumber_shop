# Generated by Django 5.1.2 on 2024-11-28 16:22

import django.db.models.deletion
import phonenumber_field.modelfields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_alter_user_age'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactinfo',
            name='Master',
        ),
        migrations.AddField(
            model_name='contactinfo',
            name='companyProfile',
            field=models.ForeignKey(default=12, on_delete=django.db.models.deletion.CASCADE, to='shop.сompanyprofile'),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Contact_Info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_info', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None)),
                ('Master', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.master')),
            ],
        ),
    ]