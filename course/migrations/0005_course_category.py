# Generated by Django 3.2.7 on 2021-09-10 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0004_alter_course_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='category',
            field=models.CharField(default='web', max_length=50),
        ),
    ]
