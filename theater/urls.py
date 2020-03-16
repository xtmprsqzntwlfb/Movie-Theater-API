from django.urls import path
from .views import ListTicketsView, ListRoomsView, ListMoviesView, ListTimeSlotsView, TimeSlotDetailView


urlpatterns = [
    path('tickets/', ListTicketsView.as_view(), name="tickets_list"),
    path('rooms/', ListRoomsView.as_view(), name="rooms_list"),
    path('movies/', ListMoviesView.as_view(), name="movies_list"),
    path('timeslots/', ListTimeSlotsView.as_view(), name="timeslots_list"),
    path('timeslots/<int:pk>/', TimeSlotDetailView.as_view(), name="timeslot_detail")
]
