# Generated by Django 4.1.4 on 2023-01-05 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pricecheckapp', '0004_alter_product_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(),
        ),
    ]
