# Generated by Django 5.0 on 2024-10-26 09:47

import account.validators
import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('id', models.UUIDField(db_column='id', db_index=True, default=uuid.uuid4, editable=False, help_text='user id', primary_key=True, serialize=False, unique=True, verbose_name='user id')),
                ('username', models.CharField(blank=True, db_column='username', db_index=True, help_text='username', max_length=150, null=True, validators=[account.validators.validate_chars], verbose_name='username')),
                ('phone', models.CharField(db_column='phone', db_comment='phone unique', db_index=True, help_text='phone', max_length=11, unique=True, validators=[account.validators.validate_phone], verbose_name='phone')),
                ('first_name', models.CharField(blank=True, db_column='first_name', db_comment='first name', db_index=True, help_text='first name', max_length=100, null=True, validators=[account.validators.validate_chars], verbose_name='first name')),
                ('last_name', models.CharField(blank=True, db_column='last_name', db_comment='last name', db_index=True, help_text='last name', max_length=100, null=True, validators=[account.validators.validate_chars], verbose_name='last name')),
                ('email', models.EmailField(blank=True, db_column='email', db_comment='email address', db_index=True, help_text='email', max_length=250, null=True, unique=True, validators=[account.validators.validate_email_address], verbose_name='email')),
                ('is_admin', models.BooleanField(db_column='is_admin', db_comment='is_admin', db_index=True, default=False, help_text='is user admin?', verbose_name='is user admin?')),
                ('is_staff', models.BooleanField(db_index=True, default=False, help_text='is user staff?', verbose_name='is user staff?')),
                ('is_active', models.BooleanField(db_column='is_active', db_comment='is_active', db_index=True, default=False, help_text='is user active?', verbose_name='is user active?')),
                ('is_superuser', models.BooleanField(db_column='is_superuser', db_comment='is_superuser', db_index=True, default=False, help_text='is user superuser?', verbose_name='is user superuser?')),
                ('date_joined', models.DateTimeField(auto_now_add=True, db_column='date_joined', db_comment='date_joined', db_index=True, help_text='date joined', verbose_name='date joined')),
                ('user_ip', models.GenericIPAddressField(blank=True, db_column='user_ip', db_comment='user_ip', db_index=True, help_text='user ip address', null=True, verbose_name='user ip address')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True, help_text='created time', verbose_name='created time')),
                ('updated', models.DateTimeField(auto_now=True, db_index=True, help_text='updated time', verbose_name='updated time')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'user',
                'ordering': ['created'],
                'get_latest_by': ['created'],
                'base_manager_name': 'objects',
            },
        ),
        migrations.CreateModel(
            name='BlockUser',
            fields=[
                ('id', models.UUIDField(db_column='id', db_index=True, default=uuid.uuid4, editable=False, help_text='code id', primary_key=True, serialize=False, unique=True, verbose_name='code id')),
                ('user_ip', models.GenericIPAddressField(blank=True, db_index=True, help_text='user ip address', null=True, verbose_name='user ip address')),
                ('blocked_time', models.DateTimeField(blank=True, db_index=True, help_text='block time', null=True, verbose_name='block time')),
                ('created', models.DateTimeField(auto_now_add=True, db_index=True, help_text='time created', verbose_name='time created')),
                ('updated', models.DateTimeField(auto_now=True, db_index=True, help_text='time updated', verbose_name='time updated')),
                ('user', models.OneToOneField(blank=True, db_column='user', help_text='user', null=True, on_delete=django.db.models.deletion.CASCADE, related_query_name='blocks', to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'blocked users',
                'verbose_name_plural': 'blocked users',
            },
        ),
        migrations.CreateModel(
            name='Code',
            fields=[
                ('id', models.UUIDField(db_column='id', db_index=True, default=uuid.uuid4, editable=False, help_text='code id', primary_key=True, serialize=False, unique=True, verbose_name='code id')),
                ('exp', models.DateTimeField(blank=True, db_index=True, help_text='expire time', null=True, verbose_name='expire time')),
                ('token', models.CharField(db_index=True, help_text='otp code', max_length=7, unique=True, verbose_name='code to verify')),
                ('user', models.OneToOneField(help_text='user', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'otp code',
                'verbose_name_plural': 'otp code',
            },
        ),
    ]
