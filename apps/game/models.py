from django.db import models
from django.contrib import admin
import datetime

class Player(models.Model):
    id = models.AutoField(primary_key=True)
    users = models.CharField(max_length=1, null=True)
    turn = models.BooleanField(default=False)
    win = models.IntegerField(null=True)
    crt_date = models.DateTimeField(default=datetime.datetime.now)

    objects = models.Manager()

    def __str__(self):
        return '{0}, {1}, {2}'.format(self.id,self.users, self.turn)


class PlayerAdmin(admin.ModelAdmin):
    list_display = ('id', 'users', 'turn', 'win','crt_date')


class Board(models.Model):
    id = models.AutoField(primary_key=True)
    column_a = models.CharField(max_length=1, null=True)
    column_b = models.CharField(max_length=1, null=True)
    column_c = models.CharField(max_length=1, null=True)

    objects = models.Manager()

    def __str__(self):
        return self.column_a


class BoardAdmin(admin.ModelAdmin):
    list_display = ('id', 'column_a', 'column_b', 'column_c')


class Move(models.Model):
    id = models.AutoField(primary_key=True)
    position = models.CharField(max_length=500,null=True)

    objects = models.Manager()

    def __str__(self):
        return self.position


class MoveAdmin(admin.ModelAdmin):
    list_display = ('id', 'position')
