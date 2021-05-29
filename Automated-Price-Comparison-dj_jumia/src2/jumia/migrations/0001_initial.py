# Generated by Django 3.1.7 on 2021-04-04 11:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jumia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=300, null=True)),
                ('manufacture', models.CharField(blank=True, max_length=50, null=True)),
                ('description', models.TextField()),
                ('img', models.TextField()),
                ('url', models.TextField()),
                ('sku', models.CharField(blank=True, max_length=50, null=True)),
                ('active', models.BooleanField(blank=True, null=True)),
                ('lastprice', models.CharField(blank=True, max_length=50, null=True)),
                ('jumiaId', models.TextField()),
                ('rate', models.FloatField()),
                ('category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='jumia', to='products.category', verbose_name='category')),
            ],
            options={
                'db_table': 'jumia',
            },
        ),
    ]
