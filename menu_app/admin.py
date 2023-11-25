from django.contrib import admin
from menu_app.models import Menu

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    list_display = ['name', 'parent', 'url']