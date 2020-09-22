from django.db import models
from django.contrib.auth.models import User


## Table for saving RaceCard details.
class RaceCard(models.Model):
    race_url = models.CharField(max_length=900,blank=True, null=True)
    horse_pedigree = models.CharField(max_length=900,blank=True, null=True)
    raceno = models.CharField(max_length=900,blank=True, null=True)
    race_primarykey = models.CharField(max_length=900,blank=True, null=True)
    main_head = models.CharField(max_length=900,blank=True, null=True)
    main_subhead = models.CharField(max_length=900,blank=True, null=True)
    race_distance = models.CharField(max_length=900,blank=True, null=True)
    is_active = models.BooleanField(default=True)
    # created_date = models.DateTimeField(auto_now_add=True)
    # created_by = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='+')
    # modified_date = models.DateTimeField(auto_now=True)
    # modified_by = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='+')