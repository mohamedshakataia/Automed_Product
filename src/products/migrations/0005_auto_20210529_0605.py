# Generated by Django 3.1.7 on 2021-05-29 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_notifyme'),
    ]

    operations = [
        migrations.AddField(
            model_name='notifyme',
            name='expectedPrice',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='notifyme',
            name='timeDate',
            field=models.DateTimeField(null=True),
        ),
    ]
