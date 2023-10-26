
from django.db import models
from django.contrib import admin
class Footballplayer (models.Model):
    eid=models.CharField(max_length=20)
    name=models.CharField(max_length=100)
    salary=models.IntegerField()
    age=models.IntegerField()
    goal=models.IntegerField()
class FootballplayerAdmin(admin.ModelAdmin):
    list_display=('eid','name','salary','age','goal')
     
