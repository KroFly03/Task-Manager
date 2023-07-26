from django.contrib import admin

from tasks.models import Task


@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'completed', 'created_at']
    list_filter = ['completed']
    readonly_fields = ['id', 'created_at']

    def get_readonly_fields(self, request, obj=None):
        if not obj:
            return self.readonly_fields + ['completed']

        return self.readonly_fields
