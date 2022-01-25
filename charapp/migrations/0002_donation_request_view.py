# Generated by Django 3.2.11 on 2022-01-25 14:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('charapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='donation_request_view',
            fields=[
                ('ngo_name', models.CharField(default=None, max_length=50, primary_key=True, serialize=False)),
                ('domain', models.CharField(default=None, max_length=50)),
                ('head_of_ngo', models.CharField(default=None, max_length=50)),
                ('contactNo', models.CharField(default=None, max_length=10)),
                ('email', models.EmailField(default=None, max_length=254)),
                ('donation_description', models.TextField(default=None)),
                ('donation_amount', models.CharField(default=None, max_length=10)),
            ],
            options={
                'db_table': 'post_request',
                'managed': False,
            },
        ),
    ]
