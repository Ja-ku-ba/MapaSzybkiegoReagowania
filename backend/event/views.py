from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from rest_framework import status

from .serializers import CreateEventSerializer
from .services import get_type_by_int


class CreateEvent(APIView):
    permission_classes = [AllowAny] 
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