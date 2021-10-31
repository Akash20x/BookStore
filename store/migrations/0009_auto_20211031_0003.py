# Generated by Django 3.2.6 on 2021-10-30 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0008_customer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='firstname',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='lastname',
        ),
        migrations.AddField(
            model_name='customer',
            name='customer_name',
            field=models.CharField(default=True, max_length=100),
        ),
        migrations.AddField(
            model_name='payment',
            name='customer_name',
            field=models.CharField(default=True, max_length=50),
        ),
        migrations.AddField(
            model_name='payment',
            name='price',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='userproduct',
            name='customer_name',
            field=models.CharField(default=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='userproduct',
            name='price',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='payment',
            name='status',
            field=models.CharField(choices=[('FAIL', 'FAIL'), ('SUCCESS', 'SUCCESS')], max_length=40),
        ),
    ]