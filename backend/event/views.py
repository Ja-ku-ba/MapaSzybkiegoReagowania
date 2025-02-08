from datetime import time, timedelta

from django.utils import timezone

from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from rest_framework import status

from .constants import C_ALL_EVENTS
from .serializers import CreateEventSerializer, EventsMarekrsSerializer
from .services import get_type_by_int, get_type_by_shorname
from .models import Event


class CreateEvent(CreateAPIView):
    permission_classes = [IsAuthenticated] 
    authentication_classes = [JWTAuthentication]
    serializer_class = CreateEventSerializer
 
    def post(self, request, *args, **kwargs):
        data = request.data.copy()
        data['creator'] = request.user.pk
        data['type'] = get_type_by_int(request.data.get('type', None))

        serializer = CreateEventSerializer(data=data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
import random
class EventsMarkers(ListAPIView):
    permission_classes = [AllowAny] 
    authentication_classes = []
    serializer_class = EventsMarekrsSerializer
 
    # def get(self, request, *args, **kwargs):
    #     data = request.data.copy()
    #     data['type'] = get_type_by_int(request.data.get('type', None))

    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def get_queryset(self):
        data = self.request.query_params.copy()
        type = data.get('type', None)
        parsed_type = get_type_by_shorname(type)
      
        if not parsed_type:
            return None
        swLat = data.get('swLat', None)
        swLong = data.get('swLong', None)
        neLat = data.get('neLat', None)
        neLong = data.get('neLong', None)
        last_five_mins = timezone.now() - timedelta(minutes=5)
        past_due_thrre_days = timezone.now() + timedelta(days=3)
        events_points = Event.objects.filter(
            type__in=parsed_type, 
            # created_at__gte=last_five_mins,
            # created_at__lte=past_due_thrre_days,
            # approved=True,
            latitiude__gte=swLat,
            latitiude__lte=neLat,
            longitude__gte=swLong,
            longitude__lte=neLong,
            banned=False
        )
        return events_points
