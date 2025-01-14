# Generated by Django 4.0.1 on 2022-01-20 16:53

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0009_post_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1)),
                ('ordered_date', models.DateField(default=django.utils.timezone.now)),
                ('status', models.CharField(choices=[('Active', 'Active'), ('Delivered', 'Delivered')], default='Active', max_length=20)),
                ('delivery_date', models.DateField(default=django.utils.timezone.now)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.customer')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.post')),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customers.restaurant')),
            ],
        ),
    ]
