# Generated by Django 2.0.7 on 2019-09-03 00:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('monsters', '0009_auto_20190902_1734'),
    ]

    operations = [
        migrations.AddField(
            model_name='monster',
            name='collab_id',
            field=models.IntegerField(default=0),
        ),
    ]
