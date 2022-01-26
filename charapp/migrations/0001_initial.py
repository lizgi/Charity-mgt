# Generated by Django 3.2.11 on 2022-01-26 10:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='donation_request_view',
            fields=[
                ('ngo_name', models.CharField(default=0, max_length=50, primary_key=True, serialize=False)),
                ('domain', models.CharField(default=0, max_length=50)),
                ('head_of_ngo', models.CharField(default=0, max_length=50)),
                ('contactNo', models.CharField(default=0, max_length=10)),
                ('email', models.EmailField(default=0, max_length=254)),
                ('donation_description', models.TextField(default=0)),
                ('donation_amount', models.CharField(default=0, max_length=10)),
            ],
            options={
                'db_table': 'post_request',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='NGO',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ngo_name', models.CharField(blank=True, max_length=30)),
                ('head_of_ngo', models.CharField(blank=True, max_length=30)),
                ('contactNo', models.CharField(blank=True, max_length=10)),
                ('email', models.EmailField(blank=True, max_length=254)),
                ('Amount', models.CharField(blank=True, max_length=30)),
                ('Reason_for_donation', models.CharField(blank=True, max_length=30)),
                ('verification_status', models.NullBooleanField(default=0)),
                ('ngo_current_user', models.CharField(blank=True, default=0, max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default=0, upload_to='profile_pics')),
                ('user', models.OneToOneField(on_delete='CASCADE', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='donation_request',
            fields=[
                ('ngo_name', models.CharField(max_length=50, primary_key=True, serialize=False)),
                ('head_of_ngo', models.CharField(blank=True, max_length=30)),
                ('contactNo', models.CharField(blank=True, max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('donation_amount', models.CharField(blank=True, default=0, max_length=15)),
                ('donation_request_user', models.CharField(blank=True, max_length=30)),
                ('Reason_for_donation_request', models.CharField(blank=True, max_length=500)),
                ('status', models.CharField(choices=[('P', 'pending'), ('A', 'Approved'), ('w', 'Withdrawn')], default='PENDING', max_length=50)),
                ('admin_approved', models.BooleanField(default=False)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='charapp.category')),
            ],
        ),
    ]
