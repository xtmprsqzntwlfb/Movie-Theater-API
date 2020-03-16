from rest_framework import serializers
from .models import Ticket, Room, Movie, TimeSlot


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ("title", "seats")


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ("title",)


class TimeSlotSerializer(serializers.ModelSerializer):
    cap = serializers.SerializerMethodField()
    room_title = serializers.CharField(source='room.title')
    movie_title = serializers.CharField(source='movie.title')

    class Meta:
        model = TimeSlot
        fields = '__all__'

    def get_cap(self, obj):
        return obj.room.seats


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = ("ticket_id", "timeslot")