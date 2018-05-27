from django.contrib import admin
from .models import Groups, Elements

@admin.register(Groups)
class GroupsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', '_name_group', 'description')
    raw_id_fields = ('parrent_group',)

    def _name_group(self, obj):
        return obj.name_group

    _name_group.short_description = 'Родительская группа'
    _name_group.admin_order_field = 'name_group'

@admin.register(Elements)
class ElementsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', '_name_group', 'created', 'moderated')
    raw_id_fields = ('parrent_group',)

    def _name_group(self, obj):
        return obj.name_group

    _name_group.short_description = 'Родительская группа'
    _name_group.admin_order_field = 'name_group'