# Generated by Django 3.0.2 on 2020-09-02 14:14

import account.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('image', models.ImageField(blank=True, null=True, upload_to=account.models.upload_location)),
                ('username', models.CharField(max_length=150, unique=True)),
                ('phone_number', models.CharField(max_length=17, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='last login')),
                ('is_active', models.BooleanField(default=True)),
                ('is_student', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name_plural': 'Account',
            },
        ),
    ]
