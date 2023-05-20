# Generated by Django 4.2.1 on 2023-05-11 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Works',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caption', models.CharField(max_length=100)),
                ('slug', models.SlugField()),
                ('body', models.TextField()),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
