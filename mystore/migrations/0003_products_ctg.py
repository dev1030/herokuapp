# Generated by Django 3.0.8 on 2020-07-16 10:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mystore', '0002_products'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='ctg',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='mystore.categorie'),
        ),
    ]
