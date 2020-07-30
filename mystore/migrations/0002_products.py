# Generated by Django 3.0.8 on 2020-07-16 10:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mystore', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product_Name', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('Description', models.TextField()),
                ('sub_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mystore.sub_categorie')),
            ],
        ),
    ]
