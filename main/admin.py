from django.contrib import admin
from .models import Group, Room
from import_export.admin import ImportExportModelAdmin



class RoomAdmin(ImportExportModelAdmin):
    list_display = ['id', 'room_name', 'capacity', 'created_at', 'updated_at']
    list_display_links = ['id', 'room_name']
    list_filter = ('room_name', 'capacity', 'created_at', 'updated_at')
    search_fields = ('room_name', )


class GroupAdmin(ImportExportModelAdmin):
    list_display = ['id', 'group_name', 'capacity', 'created_at', 'updated_at']
    list_display_links = ['id', 'group_name']
    list_filter = ('group_name', 'capacity', 'created_at', 'updated_at')
    search_fields = ('group_name', )


admin.site.register(Room, RoomAdmin)
admin.site.register(Group, GroupAdmin)
