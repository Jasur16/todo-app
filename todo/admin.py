from django.contrib import admin
from .models import TodoAppModel

@admin.register(TodoAppModel)
class TodoAppModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'status']
    list_display_links = ['title']