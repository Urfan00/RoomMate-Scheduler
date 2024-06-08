from django.urls import path
from .views import allocate_rooms


urlpatterns = [
    path("", allocate_rooms, name="index")
]
