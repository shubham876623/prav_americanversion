# Generated by Django 4.1.4 on 2023-01-05 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pricecheckapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
    ]