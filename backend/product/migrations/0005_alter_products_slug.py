# Generated by Django 5.0.4 on 2024-05-18 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_alter_products_evaluation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]