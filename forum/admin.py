from django.contrib import admin
from .models import Forum, Topic, Messages

# Register your models here.
class ForumAdmin(admin.ModelAdmin):
    list_display = ( 'all' )


admin.site.register(Forum)
admin.site.register(Topic)
admin.site.register(Messages)
