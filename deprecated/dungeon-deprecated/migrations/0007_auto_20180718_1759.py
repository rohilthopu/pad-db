# Generated by Django 2.0.7 on 2018-07-19 00:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dungeons', '0006_auto_20180717_0727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dungeontoday',
            name='listingDate',
            field=models.DateField(default=datetime.date(2018, 7, 18)),
        ),
    ]
