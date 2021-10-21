# Generated by Django 3.1 on 2020-10-04 18:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Client', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product_name', models.CharField(max_length=100)),
                ('Catagory', models.CharField(max_length=200)),
                ('cost', models.FloatField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='OrderProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_Id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Client.customer')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PetShop.addproduct')),
            ],
        ),
    ]
