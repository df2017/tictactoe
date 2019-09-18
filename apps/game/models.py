from django.db import models
from django.contrib import admin

class Player(models.Model):

    user_choices = (
        ('X', 'Cross'),
        ('O', 'Circle'),
    )

    id = models.AutoField(primary_key=True)
    users = models.CharField(max_length=1, null=True, choices=user_choices)
    turn = models.BooleanField(default=False)
    win = models.IntegerField(null=True)
    crt_date = models.DateTimeField(auto_now=True)

    objects = models.Manager()

    def __str__(self):
        return '{0}, {1}, {2}'.format(self.id,self.users, self.turn)


class PlayerAdmin(admin.ModelAdmin):
    list_display = ('id', 'users', 'turn', 'win','crt_date')


class Board(models.Model):
    id = models.AutoField(primary_key=True)
    column_1 = models.CharField(max_length=1, null=True, blank=True)
    column_2 = models.CharField(max_length=1, null=True, blank=True)
    column_3 = models.CharField(max_length=1, null=True, blank=True)
    column_4 = models.CharField(max_length=1, null=True, blank=True)
    column_5 = models.CharField(max_length=1, null=True, blank=True)
    column_6 = models.CharField(max_length=1, null=True, blank=True)
    column_7 = models.CharField(max_length=1, null=True, blank=True)
    column_8 = models.CharField(max_length=1, null=True, blank=True)
    column_9 = models.CharField(max_length=1, null=True, blank=True)
    column_10 = models.CharField(max_length=1, null=True, blank=True)
    column_11 = models.CharField(max_length=1, null=True, blank=True)
    column_12 = models.CharField(max_length=1, null=True, blank=True)
    column_13 = models.CharField(max_length=1, null=True, blank=True)
    column_14 = models.CharField(max_length=1, null=True, blank=True)
    column_15 = models.CharField(max_length=1, null=True, blank=True)
    column_16 = models.CharField(max_length=1, null=True, blank=True)

    objects = models.Manager()


    def __str__(self):
        list_display = ['id']
        for i in range(17):
            if i != 0:
                list_display.append('column_' + str(i))

        return '{0}'.format(list_display)


class BoardAdmin(admin.ModelAdmin):
    list_display = ['id']
    for i in range(17):
        if i != 0:
            list_display.append('column_' + str(i))



class Move(models.Model):
    id = models.AutoField(primary_key=True)
    position = models.CharField(max_length=500,null=True)

    objects = models.Manager()

    def __str__(self):
        return self.position


class MoveAdmin(admin.ModelAdmin):
    list_display = ('id', 'position')
