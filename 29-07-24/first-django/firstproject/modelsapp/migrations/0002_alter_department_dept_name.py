# Generated by Django 5.0.7 on 2024-07-29 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelsapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='dept_name',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]