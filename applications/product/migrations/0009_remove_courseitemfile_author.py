# Generated by Django 4.1.6 on 2023-02-24 09:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0008_alter_courseitemfile_files'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courseitemfile',
            name='author',
        ),
    ]
