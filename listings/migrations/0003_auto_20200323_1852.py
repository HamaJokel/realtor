# Generated by Django 3.0.4 on 2020-03-23 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0002_listing_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='bedrooms',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='listing',
            name='sqft',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
