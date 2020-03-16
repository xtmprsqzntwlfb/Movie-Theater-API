from rest_framework.response import Response
from rest_framework.views import status


def validate_timeslot_data(fn):
    def decorated(*args, **kwargs):
        # args[0] == GenericView Object
        time = args[0].request.data.get("time", "")
        room = args[0].request.data.get("room", "")
        movie = args[0].request.data.get("movie", "")
        if not time and not room and not movie:
            return Response(
                data={
                    "message": "Time, room and movie are required to add a timeslot"
                },
                status=status.HTTP_400_BAD_REQUEST
            )
        return fn(*args, **kwargs)
    return decorated
