# Generated by Django 3.2.8 on 2023-06-17 08:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0011_voucher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='carmodel',
            field=models.CharField(blank=True, max_length=14, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='carplate',
            field=models.CharField(blank=True, max_length=14, null=True),
        ),
    ]
