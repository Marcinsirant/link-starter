# Generated by Django 5.0.6 on 2024-05-14 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('djangoProject', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='url',
            field=models.CharField(default=1, max_length=500),
            preserve_default=False,
        ),
    ]
