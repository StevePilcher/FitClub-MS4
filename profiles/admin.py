from django.contrib import admin
from .models import UserProfile


# Register your models here.

class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'user_image_url',
        'user_image',
    )

    ordering = ('user',)


admin.site.register(UserProfile, ProfileAdmin)
