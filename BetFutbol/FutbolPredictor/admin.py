from django.contrib import admin
from .models import *

admin.site.register(League)
admin.site.register(Team)
admin.site.register(Player)
admin.site.register(Match)
admin.site.register(Prediction)
