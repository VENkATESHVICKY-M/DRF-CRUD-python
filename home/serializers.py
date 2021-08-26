from rest_framework import serializers
from .models import Users,Address


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = Users

        fields='__all__'


class AddressSerializer(serializers.ModelSerializer):

    class Meta:
        model = Address

        fields='__all__'

