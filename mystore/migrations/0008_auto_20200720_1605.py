# Generated by Django 3.0.8 on 2020-07-20 10:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mystore', '0007_auto_20200720_1604'),
    ]

    operations = [
        migrations.CreateModel(
            name='sub_categorie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_name', models.CharField(max_length=100)),
                ('catagory_name', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='mystore.categorie')),
            ],
        ),
        migrations.AddField(
            model_name='products',
            name='sub_category',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='mystore.sub_categorie'),
        ),
    ]
