# Generated by Django 3.1.1 on 2020-09-15 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_race', '0004_auto_20200915_1051'),
    ]

    operations = [
        migrations.AddField(
            model_name='race',
            name='race_distance',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='race',
            name='race_position',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='race',
            name='race_weight',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='race',
            name='race_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='race',
            name='race_name',
            field=models.TextField(blank=True, null=True),
        ),
    ]