# Generated by Django 5.0.7 on 2024-07-26 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Categories', '0002_category_parent_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='parent_category',
        ),
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]
