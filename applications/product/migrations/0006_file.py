# Generated by Django 4.1.6 on 2023-02-24 08:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_rename_file_courseitemfile_files'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.ImageField(upload_to='files/')),
                ('course_item_file', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item_files', to='product.courseitemfile')),
            ],
        ),
    ]
