# Generated by Django 4.0 on 2022-01-04 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0004_post_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='restaurant',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
