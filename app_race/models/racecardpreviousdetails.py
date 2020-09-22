from django.db import models
from django.contrib.auth.models import User


## Table for saving RacecardPreviousDetails details.
class RacecardPreviousDetails(models.Model):
    slno = models.CharField(max_length=900,blank=True, null=True)
    horse_pedigree = models.CharField(max_length=900,blank=True, null=True)
    data = models.CharField(max_length=900,blank=True, null=True)
    dist = models.CharField(max_length=900,blank=True, null=True)
    rclass = models.CharField(max_length=900,blank=True, null=True)
    raceno = models.CharField(max_length=900,blank=True, null=True)
    venue = models.CharField(max_length=900,blank=True, null=True)
    jockey = models.CharField(max_length=900,blank=True, null=True)
    wt = models.CharField(max_length=900,blank=True, null=True)
    dist_wi = models.CharField(max_length=900,blank=True, null=True)
    time = models.CharField(max_length=900,blank=True, null=True)
    rtg = models.CharField(max_length=900,blank=True, null=True)
    is_active = models.BooleanField(default=True)
    # created_date = models.DateTimeField(auto_now_add=True)
    # created_by = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='+')
    # modified_date = models.DateTimeField(auto_now=True)
    # modified_by = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='+')