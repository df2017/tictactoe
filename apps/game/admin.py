from django.contrib import admin
from .models import Player, Board,Move,BoardAdmin,PlayerAdmin,MoveAdmin
# Register your models here.

admin.site.register(Player,PlayerAdmin)
admin.site.register(Board,BoardAdmin)
admin.site.register(Move,MoveAdmin)

