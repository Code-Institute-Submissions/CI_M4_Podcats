# Generated by Django 3.0.8 on 2020-07-29 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pro', '0003_auto_20200729_1614'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='purchase_amount',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10),
        ),
        migrations.AddField(
            model_name='purchase',
            name='stripe_pid',
            field=models.CharField(default='', max_length=254),
        ),
    ]