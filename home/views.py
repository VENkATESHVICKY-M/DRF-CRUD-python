from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from rest_framework import status
from rest_framework.decorators import api_view
from django.http import Http404

from .models import Users,Address
from .serializers import UserSerializer,AddressSerializer
from home import serializers




@api_view(['GET','POST'])
def Users_av_list(request):
    if request.method == 'GET':
        user_av = Users.objects.all()
        serializer_user= UserSerializer(user_av,many = True)
        return Response(serializer_user.data)
    elif request.method == 'POST':
        serializer_user = UserSerializer(data=request.data)
        if serializer_user.is_valid():
            serializer_user.save()
            return Response(serializer_user.data,status = status.HTTP_201_CREATED)
        return Response(serializer_user.error,status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def Users_av_detail(request,pk):
    try:
        user_av = Users.objects.get(pk=pk)
    except Users.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serilizer_user = UserSerializer(user_av)
        return Response(serilizer_user.data)
    elif request.method == 'PUT':
        serializer_user = UserSerializer(user_av, data=request.data)
        if serializer_user.is_valid():
            serializer_user.save()
            return Response(serializer_user.data)
        return Response(serializer_user.error,status = status.HTTP_400_BAD_REQUEST)    
    elif request.method == 'DELETE':
        user_av.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

#------------------------------------------------------------------------------------

@api_view(['GET','POST'])
def Addresses_av_list(request):
    if request.method == 'GET':
        address_av = Address.objects.all()
        serializer_address= AddressSerializer(address_av,many = True)
        return Response(serializer_address.data)
    elif request.method == 'POST':
        serializer_address = AddressSerializer(data=request.data)
        if serializer_address.is_valid():
            serializer_address.save()
            return Response(serializer_address.data,status = status.HTTP_201_CREATED)
        return Response(serializer_address.error,status = status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def Addresses_av_detail(request,pk):
    try:
        address_av = Address.objects.get(pk=pk)
    except Address.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serilizer_address = AddressSerializer(address_av)
        return Response(serilizer_address.data)
    elif request.method == 'PUT':
        serilizer_address = AddressSerializer(address_av, data=request.data)
        if serilizer_address.is_valid():
            serilizer_address.save()
            return Response(serilizer_address.data)
        return Response(serilizer_address.error,status = status.HTTP_400_BAD_REQUEST)    
    elif request.method == 'DELETE':
        address_av.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)





















