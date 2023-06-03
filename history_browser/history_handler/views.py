from rest_framework import generics
from rest_framework.response import Response
from .serializers import HostSerializer, URLSerializer, HistorySerializer, UserSerializer
from .models import History


class HostView(generics.CreateAPIView):
    serializer_class = HostSerializer

class UserView(generics.CreateAPIView):
    serializer_class = UserSerializer

class URLView(generics.CreateAPIView):
    serializer_class = URLSerializer

class HistoryView(generics.ListCreateAPIView):
    serializer_class = HistorySerializer
    queryset = History.objects.all()

    def list(self, request, user_id):
        queryset = History.objects.select_related('user').filter(user__id=user_id)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
