# Generated by Django 5.0b1 on 2023-11-13 13:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('submissions', '0005_submission_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='submission',
            name='timestamp',
            field=models.TimeField(),
        ),
    ]
