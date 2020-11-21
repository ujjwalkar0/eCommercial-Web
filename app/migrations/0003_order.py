# Generated by Django 3.1.3 on 2020-11-20 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_post_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_id', models.IntegerField(null=True)),
                ('customer_id', models.IntegerField(null=True)),
                ('is_approved', models.BooleanField(null=True)),
            ],
        ),
    ]
