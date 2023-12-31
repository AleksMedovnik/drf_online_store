# Generated by Django 4.2.4 on 2023-08-26 14:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0002_mobilephone'),
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='orders', to=settings.AUTH_USER_MODEL)),
                ('delivery_method', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='orders', to='orders.deliverymethod')),
                ('payment_method', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='orders', to='orders.paymentmethod')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='orders', to='products.mobilephone')),
            ],
        ),
    ]
