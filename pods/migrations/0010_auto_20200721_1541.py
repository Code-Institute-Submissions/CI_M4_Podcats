# Generated by Django 3.0.8 on 2020-07-21 15:41

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('pods', '0009_auto_20200717_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='podcast',
            name='uuid',
            field=models.UUIDField(default=uuid.uuid1),
        ),
    ]
