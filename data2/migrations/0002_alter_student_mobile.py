# Generated by Django 5.0.6 on 2024-06-13 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data2', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='mobile',
            field=models.CharField(max_length=100),
        ),
    ]
