from django.db import models
import uuid


def generate_id():
    return str(uuid.uuid4()).split("-")[-1]


class Room(models.Model):
    room_id = models.CharField(max_length=255, blank=True)
    title = models.CharField(max_length=255, null=False)
    seats = models.PositiveSmallIntegerField(null=False)

    def __str__(self):
        return "{} - {} - {}".format(self.room_id, self.title, str(self.seats))

    def get_title(self):
        return self.title

    def get_cap(self):
        return self.seats

    def save(self, *args, **kwargs):
        if len(self.room_id.strip(" ")) == 0:
            self.room_id = generate_id()

        super(Room, self).save(*args, **kwargs)


class Movie(models.Model):
    movie_id = models.CharField(max_length=255, blank=True)
    title = models.CharField(max_length=255, null=False)

    def __str__(self):
        return "{} - {}".format(self.movie_id, self.title)

    def get_title(self):
        return self.title

    def save(self, *args, **kwargs):
        if len(self.movie_id.strip(" ")) == 0:
            self.movie_id = generate_id()

        super(Movie, self).save(*args, **kwargs)


class TimeSlot(models.Model):
    time = models.TimeField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE, default="-")
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, default="-")

    def __str__(self):
        return "{} - {} - {}".format(str(self.time), self.room.get_title(), self.movie.get_title())


class Ticket(models.Model):
    ticket_id = models.CharField(max_length=255, blank=True)
    timeslot = models.ForeignKey(TimeSlot, on_delete=models.CASCADE, default="")

    def __str__(self):
        return "{} - {}".format(self.ticket_id, self.timeslot)

    def save(self, *args, **kwargs):
        if len(self.ticket_id.strip(" ")) == 0:
            self.ticket_id = generate_id()

        super(Ticket, self).save(*args, **kwargs)
