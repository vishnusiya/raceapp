# Generated by Django 3.1.1 on 2020-09-22 12:57

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
            name='RaceCard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('race_url', models.CharField(blank=True, max_length=900, null=True)),
                ('horse_pedigree', models.CharField(blank=True, max_length=900, null=True)),
                ('raceno', models.CharField(blank=True, max_length=900, null=True)),
                ('race_primarykey', models.CharField(blank=True, max_length=900, null=True)),
                ('main_head', models.CharField(blank=True, max_length=900, null=True)),
                ('main_subhead', models.CharField(blank=True, max_length=900, null=True)),
                ('race_distance', models.CharField(blank=True, max_length=900, null=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='RaceCardDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no', models.CharField(blank=True, max_length=900, null=True)),
                ('silk', models.CharField(blank=True, max_length=900, null=True)),
                ('horse_pedigree', models.CharField(blank=True, max_length=900, null=True)),
                ('desc', models.CharField(blank=True, max_length=900, null=True)),
                ('owner', models.CharField(blank=True, max_length=900, null=True)),
                ('trainer', models.CharField(blank=True, max_length=900, null=True)),
                ('jockey', models.CharField(blank=True, max_length=900, null=True)),
                ('wt', models.CharField(blank=True, max_length=900, null=True)),
                ('al', models.CharField(blank=True, max_length=900, null=True)),
                ('sh', models.CharField(blank=True, max_length=900, null=True)),
                ('eq', models.CharField(blank=True, max_length=900, null=True)),
                ('rtg', models.CharField(blank=True, max_length=900, null=True)),
                ('raceno', models.CharField(blank=True, max_length=900, null=True)),
                ('race_primarykey', models.CharField(blank=True, max_length=900, null=True)),
                ('main_head', models.CharField(blank=True, max_length=900, null=True)),
                ('main_subhead', models.CharField(blank=True, max_length=900, null=True)),
                ('race_distance', models.CharField(blank=True, max_length=900, null=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='RacecardPreviousDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slno', models.CharField(blank=True, max_length=900, null=True)),
                ('horse_pedigree', models.CharField(blank=True, max_length=900, null=True)),
                ('data', models.CharField(blank=True, max_length=900, null=True)),
                ('dist', models.CharField(blank=True, max_length=900, null=True)),
                ('rclass', models.CharField(blank=True, max_length=900, null=True)),
                ('raceno', models.CharField(blank=True, max_length=900, null=True)),
                ('venue', models.CharField(blank=True, max_length=900, null=True)),
                ('jockey', models.CharField(blank=True, max_length=900, null=True)),
                ('wt', models.CharField(blank=True, max_length=900, null=True)),
                ('dist_wi', models.CharField(blank=True, max_length=900, null=True)),
                ('time', models.CharField(blank=True, max_length=900, null=True)),
                ('rtg', models.CharField(blank=True, max_length=900, null=True)),
                ('is_active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='ResultDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Pl', models.CharField(blank=True, max_length=900, null=True)),
                ('h_no', models.CharField(blank=True, max_length=900, null=True)),
                ('horse_pedigree', models.CharField(blank=True, max_length=900, null=True)),
                ('desc', models.CharField(blank=True, max_length=900, null=True)),
                ('trainer', models.CharField(blank=True, max_length=900, null=True)),
                ('jockey', models.CharField(blank=True, max_length=900, null=True)),
                ('wt', models.CharField(blank=True, max_length=900, null=True)),
                ('al', models.CharField(blank=True, max_length=900, null=True)),
                ('dr', models.CharField(blank=True, max_length=900, null=True)),
                ('sh', models.CharField(blank=True, max_length=900, null=True)),
                ('won_by', models.CharField(blank=True, max_length=900, null=True)),
                ('dist_win', models.CharField(blank=True, max_length=900, null=True)),
                ('rtg', models.CharField(blank=True, max_length=900, null=True)),
                ('odds', models.CharField(blank=True, max_length=900, null=True)),
                ('time', models.CharField(blank=True, max_length=900, null=True)),
                ('raceno', models.CharField(blank=True, max_length=900, null=True)),
                ('race_primarykey', models.CharField(blank=True, max_length=900, null=True)),
                ('main_head', models.CharField(blank=True, max_length=900, null=True)),
                ('main_subhead', models.CharField(blank=True, max_length=900, null=True)),
                ('race_distance', models.CharField(blank=True, max_length=900, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('raceno', models.CharField(blank=True, max_length=900, null=True)),
                ('race_primarykey', models.CharField(blank=True, max_length=900, null=True)),
                ('main_head', models.CharField(blank=True, max_length=900, null=True)),
                ('main_subhead', models.CharField(blank=True, max_length=900, null=True)),
                ('race_distance', models.CharField(blank=True, max_length=900, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('modified_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
