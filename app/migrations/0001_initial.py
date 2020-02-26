# Generated by Django 2.1.15 on 2020-02-25 18:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Advertisement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='ads')),
                ('item_name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=200)),
                ('quantity', models.IntegerField()),
                ('status', models.CharField(default='Not Sold', max_length=20)),
                ('category', models.CharField(choices=[('Buy', 'Buy'), ('Sell', 'Sell')], max_length=4)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
