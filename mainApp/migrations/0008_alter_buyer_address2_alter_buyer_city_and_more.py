# Generated by Django 4.0.4 on 2022-05-23 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0007_alter_buyer_address1_alter_buyer_phone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='buyer',
            name='address2',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='buyer',
            name='city',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='buyer',
            name='pin',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='buyer',
            name='state',
            field=models.CharField(max_length=20),
        ),
    ]
