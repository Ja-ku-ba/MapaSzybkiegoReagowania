from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated

from .serializers import CreateEventSerializer


class CreateEvent(CreateAPIView):
    # permission_classes = [IsAuthenticated]
    serializer_class = CreateEventSerializer
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)