from django.db import models
from django.contrib.auth.models import User


## Table for saving Horse details.
class Player(models.Model):
    horse_number = models.CharField(max_length=600,blank=True, null=True)
    player_name = models.CharField(max_length=600,blank=True, null=True)
    player_idex_num =models.CharField(max_length=600,blank=True, null=True)
    player_num = models.CharField(max_length=600,blank=True, null=True)
    player_weight = models.CharField(max_length=600,blank=True, null=True)
    player_rating = models.CharField(max_length=600,blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='+')
    modified_date = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='+')