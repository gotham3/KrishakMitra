# Generated by Django 2.1.15 on 2020-02-25 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisement',
            name='cost',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
