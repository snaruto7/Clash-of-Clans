from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class player(models.Model):    

    username = models.CharField(max_length=200,null=True)
    player_tag = models.CharField(max_length=200,null=True)
    phone_no = models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.username