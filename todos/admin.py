from django.contrib import admin

from .models import Todo

class TodoAdmin(admin.ModelAdmin):
    list_display = ('id', 'task',)
    list_display_links = list_display

admin.site.register(Todo, TodoAdmin)