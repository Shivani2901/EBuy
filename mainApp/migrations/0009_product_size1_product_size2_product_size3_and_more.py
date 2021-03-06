# Generated by Django 4.0.4 on 2022-05-24 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0008_alter_buyer_address2_alter_buyer_city_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='size1',
            field=models.CharField(blank=True, default=None, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='size2',
            field=models.CharField(blank=True, default=None, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='size3',
            field=models.CharField(blank=True, default=None, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='size4',
            field=models.CharField(blank=True, default=None, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='size5',
            field=models.CharField(blank=True, default=None, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='buyer',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='checkout',
            name='address1',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='checkout',
            name='address2',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='checkout',
            name='email',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AlterField(
            model_name='checkout',
            name='name',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AlterField(
            model_name='checkout',
            name='phone',
            field=models.CharField(default=None, max_length=15),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='seller',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]
