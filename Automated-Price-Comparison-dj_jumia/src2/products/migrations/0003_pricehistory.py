# Generated by Django 3.1.7 on 2021-05-24 02:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('souq', '0006_auto_20210404_1340'),
        ('products', '0002_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='priceHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timeDate', models.DateTimeField()),
                ('lastprice', models.CharField(blank=True, max_length=50, null=True)),
                ('souq', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='souqHis', to='souq.souq', verbose_name='souq')),
            ],
        ),
    ]