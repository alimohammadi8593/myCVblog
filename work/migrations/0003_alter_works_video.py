# Generated by Django 4.2.1 on 2023-05-13 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('work', '0002_works_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='works',
            name='video',
            field=models.FileField(blank=True, upload_to='video/%y'),
        ),
    ]
