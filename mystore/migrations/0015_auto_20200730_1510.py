# Generated by Django 3.0.8 on 2020-07-30 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mystore', '0014_brand_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='name',
            field=models.CharField(default='', max_length=100),
        ),
    ]
