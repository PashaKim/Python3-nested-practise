from django.contrib import admin
from .models import Groups, Elements

@admin.register(Groups)
class GroupsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'name_group', 'description')
    raw_id_fields = ('parrent_group',)

    def name_group(self, obj):
        return obj.name_group

    name_group.short_description = 'Родительская группа'
    name_group.admin_order_field = 'parrent_group'

@admin.register(Elements)
class ElementsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'name_group', 'created', 'moderated')
    raw_id_fields = ('parrent_group',)

    def name_group(self, obj):
        return obj.name_group

    name_group.short_description = 'Родительская группа'
    name_group.admin_order_field = 'parrent_group'