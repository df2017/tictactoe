from django.contrib import admin
from .models import Player, Board,BoardAdmin,PlayerAdmin
# Register your models here.

admin.site.register(Player,PlayerAdmin)
admin.site.register(Board,BoardAdmin)

