from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Recipe, Item, Bid

# Register your models here.

admin.site.register(User, UserAdmin)
admin.site.register(Recipe)
admin.site.register(Item)
admin.site.register(Bid)

