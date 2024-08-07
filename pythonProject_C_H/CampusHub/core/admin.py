from django.contrib import admin

from .models import Item, Category


class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'image', 'price', 'stock')


admin.site.register(Item, ItemAdmin)
admin.site.register(Category)