from django.db import models



class Group(models.Model):
    group_name = models.CharField(max_length=100)
    capacity = models.PositiveIntegerField()

    def __str__(self):
        return self.group_name


class Room(models.Model):
    room_name = models.CharField(max_length=100)
    capacity = models.PositiveIntegerField()

    def __str__(self):
        return self.room_name
