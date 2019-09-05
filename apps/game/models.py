from django.db import models
from django.contrib import admin


class Player(models.Model):
    idp = models.AutoField(primary_key=True)
    users = models.CharField(max_length=1, null=True)
    turn = models.BooleanField(default=False)
    win = models.IntegerField(max_length=1000)
    crt_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return (self.idp, self.users)


class PlayerAdmin(admin.ModelAdmin):
    list_display = ('idp', 'users', 'turn', 'win')


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
    position = models.CharField(max_length=2000,null=True)
