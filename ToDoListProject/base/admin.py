from django.contrib import admin
from .models import Task

class TaskAdmin(admin.ModelAdmin):
    model = Task
    list_display = ['user', 'title', 'description', 'complete', 'created', 'updated']
    list_filter = ['complete', 'created']
    search_fields = ['title']

admin.site.register(Task, TaskAdmin)
