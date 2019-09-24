from django.contrib import admin
from .models import Groups, Elements


@admin.register(Groups)
class GroupsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name',  'parent_group', 'description')
    raw_id_fields = ('parent_group',)
    list_filter = ('parent_group', )


@admin.register(Elements)
class ElementsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'group', 'created', 'moderated')
    raw_id_fields = ('group',)
