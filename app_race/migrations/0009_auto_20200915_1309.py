# Generated by Django 3.1.1 on 2020-09-15 13:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_race', '0008_auto_20200915_1304'),
    ]

    operations = [
        migrations.RenameField(
            model_name='race',
            old_name='race_name',
            new_name='player_name',
        ),
    ]
