# Generated by Django 4.1.6 on 2023-02-24 08:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_alter_course_language_alter_courseitemfile_file'),
    ]

    operations = [
        migrations.RenameField(
            model_name='courseitemfile',
            old_name='file',
            new_name='files',
        ),
    ]
