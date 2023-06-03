from rest_framework import generics
from rest_framework.response import Response
from .serializers import HostSerializer, URLSerializer, HistorySerializer, UserSerializer
from .models import History
from .decorators import multi_create


class HostView(generics.CreateAPIView):
    serializer_class = HostSerializer

    @multi_create(serializer_class=HostSerializer)
    def create(self, request):
        pass

class UserView(generics.CreateAPIView):
    serializer_class = UserSerializer

class URLView(generics.CreateAPIView):
    serializer_class = URLSerializer

    @multi_create(serializer_class=URLSerializer)
    def create(self, request):
        pass

class HistoryView(generics.ListCreateAPIView):
    serializer_class = HistorySerializer
    queryset = History.objects.all() # TODO: unify

    def list(self, request, user_id):
        queryset = History.objects.select_related('user').filter(user__id=user_id) # TODO: unify
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @multi_create(serializer_class=HistorySerializer)
    def create(self, request, user_id):
        pass