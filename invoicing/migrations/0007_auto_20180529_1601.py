# Generated by Django 2.0.3 on 2018-05-29 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoicing', '0006_auto_20180529_1224'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='total',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='invoice',
            name='vat',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10),
        ),
    ]
