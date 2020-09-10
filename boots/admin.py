from django.contrib import admin
from .models import Boot, Brand, Review

# Register your models here.


class BootAdmin(admin.ModelAdmin):
    list_display = (
        'style',
        'name',
        'category',
        'price',
        'colour',
        'image',
    )

    ordering = ('style',)


class BrandAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


class ReviewAdmin(admin.ModelAdmin):
    list_display = (
        'boot',
        'name',
        'comment',
        'rating',
    )


admin.site.register(Boot, BootAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Review, ReviewAdmin)
