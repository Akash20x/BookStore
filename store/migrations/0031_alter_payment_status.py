# Generated by Django 3.2.6 on 2021-10-31 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0030_auto_20211101_0053'),
    ]

    operations = [
        migrations.AlterField(
            model_name='payment',
            name='status',
            field=models.CharField(choices=[('FAIL', 'FAIL'), ('SUCCESS', 'SUCCESS')], max_length=40),
        ),
    ]
