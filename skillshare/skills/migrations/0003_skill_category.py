# Generated by Django 5.1.1 on 2024-10-10 13:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('skills', '0002_job'),
    ]

    operations = [
        migrations.AddField(
            model_name='skill',
            name='category',
            field=models.CharField(default='General', max_length=255),
        ),
    ]
