from rest_framework import serializers
from .models import Host, URL, User, History

class HostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Host
        fields = ['hostname']

class URLSerializer(serializers.ModelSerializer):
    class Meta:
        model = URL
        fields = ['url', 'title', 'host_id']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username']

class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = ['url', 'user']
