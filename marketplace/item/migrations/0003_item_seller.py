# Generated by Django 5.0.3 on 2024-03-14 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('item', '0002_alter_category_options_item'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='seller',
            field=models.TextField(blank=True, null=True),
        ),
    ]