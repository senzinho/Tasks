from django.contrib import admin
from task.models import tasks

class TaskAdmin(admin.ModelAdmin):
    list_display = ('task_name','task_description','task_date')
    search_fields = ('task_name','task_date')

admin.site.register(tasks, TaskAdmin)