# Generated by Django 3.2.7 on 2021-09-11 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0006_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='email',
            field=models.CharField(default='', max_length=50),
        ),
    ]
