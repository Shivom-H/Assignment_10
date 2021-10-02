# Generated by Django 3.2.7 on 2021-09-10 05:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_auto_20210909_2106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='image',
            field=models.ImageField(default='', upload_to='course\\images'),
        ),
        migrations.AlterField(
            model_name='course',
            name='pub_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]