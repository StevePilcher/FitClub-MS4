from django.contrib import admin
from .models import Forum, Conversation


# Register your models here.
class ForumAdmin(admin.ModelAdmin):
    list_display = (
        'topic',
        'date_time',
    )

    ordering = ('date_time',)


admin.site.register(Forum, ForumAdmin)
admin.site.register(Conversation)
