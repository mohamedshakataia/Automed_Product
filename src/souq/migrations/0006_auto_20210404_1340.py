# Generated by Django 3.1.7 on 2021-04-04 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('souq', '0005_souq_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='souq',
            name='manufacture',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]