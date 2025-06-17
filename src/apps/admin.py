from django.contrib import admin

from .models import MenuModel


class MenuModelAdmin(admin.ModelAdmin):
	list_display = ('name', 'menu_name', 'url', 'named_url')
	list_filter = ('menu_name',)

admin.site.register(MenuModel, MenuModelAdmin)