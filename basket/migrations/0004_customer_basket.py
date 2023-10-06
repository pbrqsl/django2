# Generated by Django 4.2.5 on 2023-10-02 20:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('basket', '0003_remove_customer_basket'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='basket',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='basket.basket'),
        ),
    ]
