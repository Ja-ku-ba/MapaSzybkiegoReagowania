from django.urls import path, include

from .views import CreateEvent, EventsMarkers


urlpatterns = [
    path('create/', CreateEvent.as_view()),
    path('map-markers/', EventsMarkers.as_view()),
]
