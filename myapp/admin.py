from django.contrib import admin
from . import models

class TodoAdmin(admin.ModelAdmin):
    list_display = ('task', 'date', 'status', 'created_at', 'updated_at', 'is_active')

admin.site.register(models.Todo, TodoAdmin)
