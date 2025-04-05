# Generated by Django 5.2 on 2025-04-05 16:27

import django.db.models.deletion
import phonenumber_field.modelfields
import user.models
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('business', '0005_customerpersonnel'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('id', models.CharField(default=uuid.uuid4, editable=False, max_length=255, primary_key=True, serialize=False)),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='email address')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, region=None, unique=True, verbose_name='phone number')),
                ('first_name', models.CharField(max_length=255, verbose_name='first name')),
                ('middle_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='middle name')),
                ('last_name', models.CharField(max_length=255, verbose_name='last name')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('hand_held_device_token', models.CharField(blank=True, max_length=255, null=True)),
                ('user_profile_image', models.ImageField(blank=True, null=True, upload_to='user_profile_images/')),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('groups', models.ManyToManyField(blank=True, related_name='custom_user_set', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, related_name='custom_user_set', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'ordering': ['-created_date'],
            },
            managers=[
                ('objects', user.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='DeliveryStaff',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None)),
                ('gender', models.IntegerField(choices=[(1, 'Female'), (2, 'Male'), (3, 'Unknown')], default=3)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_suspended', models.BooleanField(default=False)),
                ('business', models.ManyToManyField(blank=True, related_name='business_delivery_staff', to='business.business')),
                ('location', models.ManyToManyField(blank=True, related_name='location_delivery_staff', to='business.location')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='delivery_staff_profiles', to='user.customuser')),
            ],
            options={
                'ordering': ['-created_date'],
            },
        ),
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None)),
                ('gender', models.IntegerField(choices=[(1, 'Female'), (2, 'Male'), (3, 'Unknown')], default=3)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_suspended', models.BooleanField(default=False)),
                ('business', models.ManyToManyField(blank=True, related_name='business_regional_managers', to='business.business')),
                ('location', models.ManyToManyField(blank=True, related_name='location_regional_managers', to='business.location')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='manager_profiles', to='user.customuser')),
            ],
            options={
                'ordering': ['-created_date'],
            },
        ),
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None)),
                ('gender', models.IntegerField(choices=[(1, 'Female'), (2, 'Male'), (3, 'Unknown')], default=3)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_suspended', models.BooleanField(default=False)),
                ('business', models.ManyToManyField(blank=True, related_name='business_owners', to='business.business')),
                ('location', models.ManyToManyField(blank=True, related_name='location_owners', to='business.location')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner_profiles', to='user.customuser')),
            ],
            options={
                'ordering': ['-created_date'],
            },
        ),
        migrations.CreateModel(
            name='SalesAgent',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None)),
                ('gender', models.IntegerField(choices=[(1, 'Female'), (2, 'Male'), (3, 'Unknown')], default=3)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_suspended', models.BooleanField(default=False)),
                ('business', models.ManyToManyField(blank=True, related_name='business_sales_agents', to='business.business')),
                ('location', models.ManyToManyField(blank=True, related_name='location_sales_agents', to='business.location')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sales_agent_profiles', to='user.customuser')),
            ],
            options={
                'ordering': ['-created_date'],
            },
        ),
        migrations.CreateModel(
            name='Supervisor',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None)),
                ('gender', models.IntegerField(choices=[(1, 'Female'), (2, 'Male'), (3, 'Unknown')], default=3)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_suspended', models.BooleanField(default=False)),
                ('business', models.ManyToManyField(blank=True, related_name='business_supervisors', to='business.business')),
                ('location', models.ManyToManyField(blank=True, related_name='location_supervisors', to='business.location')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='supervisor_profiles', to='user.customuser')),
            ],
            options={
                'ordering': ['-created_date'],
            },
        ),
        migrations.CreateModel(
            name='SupportAnalyst',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None)),
                ('gender', models.IntegerField(choices=[(1, 'Female'), (2, 'Male'), (3, 'Unknown')], default=3)),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_suspended', models.BooleanField(default=False)),
                ('business', models.ManyToManyField(blank=True, related_name='business_support_analysts', to='business.business')),
                ('location', models.ManyToManyField(blank=True, related_name='location_support_analysts', to='business.location')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='support_analyst_profiles', to='user.customuser')),
            ],
            options={
                'ordering': ['-created_date'],
            },
        ),
    ]
