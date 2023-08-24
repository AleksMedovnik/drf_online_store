# Generated by Django 4.2.4 on 2023-08-22 12:48

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('categories', '0001_initial'),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MobilePhone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(db_index=True, max_length=255)),
                ('info', models.TextField(blank=True)),
                ('price', models.FloatField(default=0, validators=[django.core.validators.MaxValueValidator(1000000000.0), django.core.validators.MinValueValidator(0)])),
                ('screen_diagonal', models.FloatField()),
                ('battery_capacity', models.IntegerField()),
                ('resolution_main_camera', models.FloatField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='categories.category')),
                ('color', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='products.color')),
                ('maker', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='products', to='products.maker')),
                ('os', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='products', to='products.os')),
                ('ram', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='products', to='products.ram')),
            ],
            options={
                'db_table': 'mobile_phones',
            },
        ),
    ]
