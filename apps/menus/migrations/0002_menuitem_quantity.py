# Generated by Django 5.1.3 on 2024-11-23 04:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='menuitem',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
    ]
