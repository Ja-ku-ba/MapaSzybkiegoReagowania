from django.urls import path, include

from .views import CreateEvent, EventsMarkers, GetLocationCords


urlpatterns = [
    path('create/', CreateEvent.as_view()),
    path('map-markers/', EventsMarkers.as_view()),
    path('location/', GetLocationCords.as_view())
]
