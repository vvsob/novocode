# Generated by Django 5.0b1 on 2023-11-18 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compilers', '0002_compiler_file_extension'),
    ]

    operations = [
        migrations.AlterField(
            model_name='compiler',
            name='name',
            field=models.CharField(max_length=256, null=True),
        ),
    ]
