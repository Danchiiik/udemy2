# Generated by Django 4.1.6 on 2023-02-21 17:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_alter_course_sub_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='category',
            field=models.ForeignKey(default='Programming', on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='product.category'),
        ),
    ]