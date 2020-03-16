from rest_framework import generics, filters
from rest_framework.response import Response
from rest_framework.views import status
from .models import Ticket, Room, Movie, TimeSlot
from .serializers import TicketSerializer, RoomSerializer, MovieSerializer, TimeSlotSerializer
from .utils import validate_timeslot_data


class ListTicketsView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer


class ListRoomsView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class ListMoviesView(generics.ListAPIView):
    """
    Provides a get method handler.
    """
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer


class ListTimeSlotsView(generics.ListAPIView):
    serializer_class = TimeSlotSerializer

    search_fields = ['time', 'movie__title', 'room__title']
    filter_backends = (filters.SearchFilter,)
    queryset = TimeSlot.objects.all()


class TimeSlotDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TimeSlot.objects.all()
    serializer_class = TimeSlotSerializer

    def get(self, request, *args, **kwargs):
        try:
            timeslot = self.queryset.get(pk=kwargs["pk"])
            return Response(TimeSlotSerializer(timeslot).data)
        except TimeSlot.DoesNotExist:
            return Response(
                data={
                    "message": "Timeslot with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )

    @validate_timeslot_data
    def put(self, request, *args, **kwargs):
        try:
            timeslot = self.queryset.get(pk=kwargs["pk"])
            serializer = TimeSlotSerializer()
            updated_song = serializer.update(timeslot, request.data)
            return Response(TimeSlotSerializer(updated_song).data)
        except TimeSlot.DoesNotExist:
            return Response(
                data={
                    "message": "Timeslot with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )

    def delete(self, request, *args, **kwargs):
        try:
            timeslot = self.queryset.get(pk=kwargs["pk"])
            timeslot.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except TimeSlot.DoesNotExist:
            return Response(
                data={
                    "message": "Timeslot with id: {} does not exist".format(kwargs["pk"])
                },
                status=status.HTTP_404_NOT_FOUND
            )
