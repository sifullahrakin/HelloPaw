# Generated by Django 3.0.3 on 2020-10-15 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('PetService', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='service_cost',
            field=models.CharField(max_length=10),
        ),
    ]
