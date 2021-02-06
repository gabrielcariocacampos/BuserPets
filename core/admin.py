from django.contrib import admin

from core.models import ActivityLog, Todo, Animais


class ActivityLogAdmin(admin.ModelAdmin):
    list_display = ('type', 'logged_user', 'created_at')

class TodoAdmin(admin.ModelAdmin):
    list_display = ('description', 'done')

class AnimaisAdmin(admin.ModelAdmin):
    list_display = ('nomeanimal', 'raça', 'costumes', 'alimentação', 'gosta', 'idade')


admin.site.register(ActivityLog, ActivityLogAdmin)
admin.site.register(Todo, TodoAdmin)
admin.site.register(Animais, AnimaisAdmin)