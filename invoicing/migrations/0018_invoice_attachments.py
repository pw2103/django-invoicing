# Generated by Django 2.0.6 on 2018-06-19 12:15

from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('invoicing', '0017_auto_20180619_1349'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='attachments',
            field=jsonfield.fields.JSONField(blank=True, default=None, null=True),
        ),
    ]
