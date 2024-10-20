# Generated by Django 5.0.7 on 2024-07-26 15:22

import multiselectfield.db.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Suppliers', '0004_supplier_active_supplier_city_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='supplier',
            name='services_offered',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Delivery', 'Delivery'), ('Installation', 'Installation'), ('Warranty', 'Warranty'), ('Support', 'Support'), ('Maintenance', 'Maintenance')], max_length=50, null=True),
        ),
    ]
