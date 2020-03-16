from django.contrib import admin
from .models import Ticket, Room, Movie, TimeSlot

admin.site.register(Ticket)
admin.site.register(Room)
admin.site.register(Movie)
admin.site.register(TimeSlot)
