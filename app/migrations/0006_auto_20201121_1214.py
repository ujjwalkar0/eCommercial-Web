# Generated by Django 3.1.3 on 2020-11-21 12:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20201121_1209'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='is_approved',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
