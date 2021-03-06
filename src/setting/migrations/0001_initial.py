# Generated by Django 3.1.7 on 2021-05-27 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('logo', models.ImageField(upload_to='info/')),
                ('description', models.TextField(max_length=300)),
                ('fb_link', models.URLField()),
                ('twitter_link', models.URLField()),
                ('instagram_link', models.URLField()),
                ('adress', models.TextField(max_length=200)),
                ('phone_number', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=60)),
            ],
            options={
                'verbose_name': 'Info',
                'verbose_name_plural': 'Infos',
            },
        ),
    ]
