from django.contrib import admin
from .models import Group, Room


class RoomAdmin(admin.ModelAdmin):
    list_display = ['id', 'room_name', 'capacity']


class GroupAdmin(admin.ModelAdmin):
    list_display = ['id', 'group_name', 'capacity']


admin.site.register(Room, RoomAdmin)
admin.site.register(Group, GroupAdmin)
