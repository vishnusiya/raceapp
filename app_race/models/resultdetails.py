from django.db import models
from django.contrib.auth.models import User


## Table for saving Result details.
class ResultDetails(models.Model):
    Pl = models.CharField(max_length=900,blank=True, null=True)
    h_no = models.CharField(max_length=900,blank=True, null=True)
    horse_pedigree = models.CharField(max_length=900,blank=True, null=True)
    desc = models.CharField(max_length=900,blank=True, null=True)
    trainer = models.CharField(max_length=900,blank=True, null=True)
    jockey = models.CharField(max_length=900,blank=True, null=True)
    wt = models.CharField(max_length=900,blank=True, null=True)
    al = models.CharField(max_length=900,blank=True, null=True)
    dr = models.CharField(max_length=900,blank=True, null=True)
    sh = models.CharField(max_length=900,blank=True, null=True)
    won_by = models.CharField(max_length=900,blank=True, null=True)
    dist_win = models.CharField(max_length=900,blank=True, null=True)
    rtg = models.CharField(max_length=900,blank=True, null=True)
    odds = models.CharField(max_length=900,blank=True, null=True)
    time = models.CharField(max_length=900,blank=True, null=True)
    raceno = models.CharField(max_length=900,blank=True, null=True)
    race_primarykey = models.CharField(max_length=900,blank=True, null=True)
    main_head = models.CharField(max_length=900,blank=True, null=True)
    main_subhead = models.CharField(max_length=900,blank=True, null=True)
    race_distance = models.CharField(max_length=900,blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='+')
    modified_date = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='+')