# Generated by Django 4.1.6 on 2023-02-18 13:04

import applications.account.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=225)),
                ('is_active', models.BooleanField(default=False)),
                ('is_mentor', models.BooleanField(default=False)),
                ('expierence', models.PositiveIntegerField(blank=True, null=True)),
                ('audience', models.CharField(blank=True, choices=[('в настоящий момент нет', 'в настоящий момент нет'), ('у меня маленькая аудитория', 'у меня маленькая аудитория'), ('у меня достаточная аудитория', 'у меня достаточная аудитория')], max_length=100, null=True)),
                ('type', models.CharField(blank=True, choices=[('лично, частным образом', 'лично, частным образом'), ('лично, профессионально', 'лично, профессионально'), ('онлайн', 'онлайн'), ('другое', 'другое')], max_length=100, null=True)),
                ('activation_code', models.CharField(blank=True, max_length=40)),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('password_reset_requested_at', models.DateTimeField(blank=True, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', applications.account.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('competence', models.CharField(max_length=100)),
                ('language', models.CharField(max_length=20)),
                ('site_url', models.CharField(blank=True, max_length=50, null=True)),
                ('twitter_url', models.CharField(blank=True, max_length=50, null=True)),
                ('facebook_url', models.CharField(blank=True, max_length=50, null=True)),
                ('linkedin_url', models.CharField(blank=True, max_length=50, null=True)),
                ('youtube_url', models.CharField(blank=True, max_length=50, null=True)),
                ('image', models.CharField(blank=True, max_length=150, null=True)),
                ('is_hidden', models.BooleanField(default=False)),
                ('is_hidden_courses', models.BooleanField(default=False)),
                ('promotions', models.BooleanField(default=False)),
                ('mentor_ads', models.BooleanField(default=False)),
                ('email_ads', models.BooleanField(default=False)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='profiles', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
