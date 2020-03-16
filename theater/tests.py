from django.urls import reverse

from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from .models import Movie, Room, TimeSlot, Ticket
from .serializers import MovieSerializer, RoomSerializer, \
    TimeSlotSerializer, TicketSerializer


class BaseModelTest(APITestCase):
    def setUp(self):
        self.room = Room.objects.create(
            title="Black",
            seats=2
        )

        self.movie = Movie.objects.create(
            title="Rose"
        )

    def test_room(self):
        """"
        This test ensures that the objects created in the setUp exist
        """
        self.assertEqual(self.room.title, "Black")
        self.assertEqual(self.room.seats, 2)

        self.assertEqual(self.movie.title, "Rose")


class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_room(title="", seats=42):
        if title != "" and seats > 0:
            Room.objects.create(title=title, seats=seats)

    @staticmethod
    def create_movie(title=""):
        if title != "":
            Movie.objects.create(title=title)

    @staticmethod
    def create_timeslot(time="", room="", movie=""):
        if time != "" and room != "" and movie != "":
            TimeSlot.objects.create(time=time, room=room, movie=movie)

    @staticmethod
    def create_ticket(timeslot=""):
        if timeslot != "":
            Ticket.objects.create(timeslot=timeslot)

    def setUp(self):
        # add test data
        self.create_room("Black", 2)
        self.create_room("White", 2)

        self.create_movie("Rose")
        self.create_movie("Lily")

        self.create_timeslot(
            "00:00:00", Room.objects.all()[0], Movie.objects.all()[0])

        self.create_ticket(TimeSlot.objects.all()[0])


class GetAllObjectsTest(BaseViewTest):
    """
    The tests below ensure that all objects added in the setUp method
    exist when we make a GET request to the corresponding endpoint
    """
    def test_get_all_rooms(self):
        # hit the API endpoint
        response = self.client.get(
            reverse("rooms_list", kwargs={"version": "v1"})
        )
        # fetch the data from db
        expected = Room.objects.all()
        serialized = RoomSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_all_movies(self):
        response = self.client.get(
            reverse("movies_list", kwargs={"version": "v1"})
        )

        expected = Movie.objects.all()
        serialized = MovieSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_all_timeslots(self):
        response = self.client.get(
            reverse("timeslots_list", kwargs={"version": "v1"})
        )

        expected = TimeSlot.objects.all()
        serialized = TimeSlotSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_all_tickets(self):
        response = self.client.get(
            reverse("tickets_list", kwargs={"version": "v1"})
        )

        expected = Ticket.objects.all()
        serialized = TicketSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
