# Generated by Django 5.0.4 on 2024-05-14 08:11

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('title', models.CharField(max_length=100)),
                ('category_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('slug', models.SlugField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, default='', null=True, upload_to='img-category')),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('discount', models.BooleanField(default=False)),
                ('image', models.ImageField(blank=True, default='', null=True, upload_to='img')),
                ('old_price', models.FloatField(default=100.0)),
                ('slug', models.SlugField(default=None)),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='product.category')),
            ],
        ),
    ]
