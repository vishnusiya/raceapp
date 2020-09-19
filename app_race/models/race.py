from django.db import models
from django.contrib.auth.models import User
from .player import Player


## Table for saving Race details.
class Race(models.Model):
    player_name = models.CharField(max_length=200,blank=True, null=True)
    race_class = models.TextField(blank=True, null=True,)
    race_position = models.CharField(max_length=200,blank=True, null=True)
    race_distance = models.TextField(blank=True, null=True)
    race_rating = models.TextField(blank=True, null=True)
    race_weight = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    race_date = models.TextField(blank=True, null=True)    
    is_active = models.BooleanField(default=True)
    created_date = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='+')
    modified_date = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='+')