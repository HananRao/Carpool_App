# Generated by Django 3.2.8 on 2023-06-04 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0003_remove_privateroom_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='privateroom',
            name='name',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='privateroom',
            name='msg',
            field=models.CharField(max_length=500),
        ),
    ]
