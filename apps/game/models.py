from django.db import models
from rest_framework import serializers
# Create your models here.
class Player(models.Model):
    idp = models.AutoField(primary_key=True)
    users = models.CharField(max_length=1, null=True)
    turn = models.BooleanField(default=False)
    crt_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return (self.idp,self.users)

class Board(models.Model):
    column_a = models.CharField(max_length=1,null=True)
    column_b = models.CharField(max_length=1,null=True)
    column_c = models.CharField(max_length=1,null=True)

    def __str__(self):
        return '%s %s %s'%(self.column_a,self.column_b,self.column_c)

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = '__all__'