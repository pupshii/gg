# Generated by Django 4.0.4 on 2022-05-13 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HotelApp', '0016_alter_payment_payment_allprice_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='Transaction_Review',
            field=models.BooleanField(default=False),
        ),
    ]