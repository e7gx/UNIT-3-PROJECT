# Generated by Django 5.0.7 on 2024-07-27 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Suppliers', '0008_supplier_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='supplier',
            name='policy',
            field=models.CharField(blank=True, choices=[('No Returns', 'No Returns'), ('Exchange Only', 'Exchange Only'), ('Refund Only', 'Refund Only'), ('Exchange or Refund', 'Exchange or Refund')], max_length=50, null=True),
        ),
    ]