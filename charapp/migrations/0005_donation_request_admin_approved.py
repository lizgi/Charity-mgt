# Generated by Django 3.2.9 on 2022-01-26 07:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charapp', '0004_auto_20220126_0724'),
    ]

    operations = [
        migrations.AddField(
            model_name='donation_request',
            name='admin_approved',
            field=models.BooleanField(default=False),
        ),
    ]