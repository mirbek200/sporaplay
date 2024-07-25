# Generated by Django 5.0.6 on 2024-06-16 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0005_roombase'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='roombase',
            name='room',
        ),
        migrations.AddField(
            model_name='roombase',
            name='room_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
