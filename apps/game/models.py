from django.db import models
from django.contrib import admin
import datetime

class Player(models.Model):
    idp = models.AutoField(primary_key=True)
    users = models.CharField(max_length=1, null=True)
    turn = models.BooleanField(default=False)
    win = models.IntegerField(null=True)
    crt_date = models.DateTimeField(default=datetime.datetime.now)

    def __str__(self):
        return (self.idp, self.users)


class PlayerAdmin(admin.ModelAdmin):
    list_display = ('idp', 'users', 'turn', 'win','crt_date')


class Board(models.Model):
    column_a = models.CharField(max_length=1, null=True)
    column_b = models.CharField(max_length=1, null=True)
    column_c = models.CharField(max_length=1, null=True)

    def __str__(self):
        return self.column_a


class BoardAdmin(admin.ModelAdmin):
    list_display = ('id', 'column_a', 'column_b', 'column_c')


class Move(models.Model):
    idm = models.AutoField(primary_key=True)
    position = models.CharField(max_length=500,null=True)

class MoveAdmin(admin.ModelAdmin):
    list_display = ('idm', 'position')
