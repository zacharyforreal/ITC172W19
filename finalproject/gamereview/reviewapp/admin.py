from django.contrib import admin
from .models import GameType, Game, Review

# Register your models here.
admin.site.register(GameType)
admin.site.register(Game)
admin.site.register(Review)