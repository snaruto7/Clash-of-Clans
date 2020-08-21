from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class player(models.Model):    

    username = models.CharField(max_length=200,primary_key=True)
    player_tag = models.CharField(max_length=200,null=True)
    phone_no = models.CharField(max_length=200,null=True)
    clan = models.CharField(max_length=200,null=True)
    role = models.CharField(max_length=200,null=True)
    attackWins = models.IntegerField(null=True)
    defenseWins = models.IntegerField(null=True)
    townHallLevel = models.IntegerField(null=True)
    versusBattleWins = models.IntegerField(null=True)
    expLevel = models.IntegerField(null=True)
    trophies = models.IntegerField(null=True)
    bestTrophies = models.IntegerField(null=True)
    donations = models.IntegerField(null=True)
    donationsReceived = models.IntegerField(null=True)
    builderHallLevel = models.IntegerField(null=True)
    versusTrophies = models.IntegerField(null=True)
    bestVersusTrophies = models.IntegerField(null=True)
    warStars = models.IntegerField(null=True)
    versusBattleWinCount = models.IntegerField(null=True)

    def __str__(self):
        return self.username
