from django.contrib import admin
from .models import Groups, Elements

@admin.register(Groups)
class GroupsAdmin(admin.ModelAdmin):
    list_display = ('name', 'parrent_group')
    raw_id_fields = ('parrent_group',)

@admin.register(Elements)
class ElementsAdmin(admin.ModelAdmin):
    list_display = ('name', 'parrent_group', 'created', 'moderated')
    raw_id_fields = ('parrent_group',)