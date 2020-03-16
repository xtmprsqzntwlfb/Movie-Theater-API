## Movie theater API

Django-based API for a simple movie theater service:

* Rooms with a designated capacity
* Movies 
* Time slots to set movie for a corresponding room and time
* Tickets for movies at a set room and time

## Installation Pre-requisites:

* Django
* Django REST Framework

## Usage

Clone the repo:
```
git clone https://github.com/xtmprsqzntwlfb/Movie-Theater-API.git
```
Install virtual environment and activate it:
```
cd Movie-Theater-API/
python3 -m venv venv
source venv/bin/activate
```
Install requirements:
```
pip install django djangorestframework
```
Run server:
```
python manage.py runserver
```
Open a browser and go to ```127.0.0.1:8000/admin``` with admin/admin credentials

Endpoints:

```
http://127.0.0.1:8000/api/v1/rooms
http://127.0.0.1:8000/api/v1/movies
http://127.0.0.1:8000/api/v1/timeslots
http://127.0.0.1:8000/api/v1/tickets
```

Details:

```
127.0.0.1:8000/api/v1/timeslots/<id>
```

Filters:

```
http://127.0.0.1:8000/api/v1/timeslots/?search=Black
```
