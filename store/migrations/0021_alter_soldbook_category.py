# Generated by Django 3.2.6 on 2021-10-31 14:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0020_alter_payment_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='soldbook',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.category'),
        ),
    ]
