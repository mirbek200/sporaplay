# Generated by Django 5.0.6 on 2024-05-31 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='max_players',
            field=models.IntegerField(default=4),
        ),
        migrations.AddField(
            model_name='room',
            name='room_name',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
