from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Recipe, Item, QuestionAnswer

# Register your models here.

admin.site.register(User, UserAdmin)
admin.site.register(Recipe)
admin.site.register(Item)

@admin.register(QuestionAnswer)
class QuestionAnswerAdmin(admin.ModelAdmin):
    list_display = ['time', 'sender', 'recip', 'text']
    ordering = ['-time']
