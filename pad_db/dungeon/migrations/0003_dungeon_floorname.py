# Generated by Django 2.0.7 on 2018-12-11 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dungeon', '0002_dungeon_possibledrops'),
    ]

    operations = [
        migrations.AddField(
            model_name='dungeon',
            name='floorName',
            field=models.CharField(default='', max_length=50),
        ),
    ]
