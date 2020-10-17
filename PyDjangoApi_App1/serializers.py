from rest_framework import serializers

from PyDjangoApi_App1 import models


class HelloSerializer(serializers.Serializer):
    """Serializes a name field for testing out APIView"""
    name = serializers.CharField(max_length=10)
