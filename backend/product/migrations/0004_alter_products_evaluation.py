# Generated by Django 5.0.4 on 2024-05-14 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0003_alter_products_evaluation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='evaluation',
            field=models.IntegerField(choices=[(0, 'Zero Star'), (1, 'One Star'), (2, 'Two Stars'), (3, 'Three Stars'), (4, 'Four Stars'), (5, 'Five Stars')], default=0),
        ),
    ]
