# Generated by Django 3.2.6 on 2021-10-30 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_auto_20211031_0003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='status',
            field=models.CharField(choices=[('SUCCESS', 'SUCCESS'), ('FAIL', 'FAIL')], max_length=40),
        ),
    ]
