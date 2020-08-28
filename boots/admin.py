from django.contrib import admin
from .models import Boot, Brand

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


admin.site.register(Boot, BootAdmin)
admin.site.register(Brand, BrandAdmin)
