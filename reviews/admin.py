from django.contrib import admin
from reviews.models import Review


# Register your models here.

class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'review_title',
        'sku',
    )

    ordering = ('sku',)


admin.site.register(Review, ReviewAdmin)
