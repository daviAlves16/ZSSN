from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


from .models import User, Itens, Inventario
from .serializers import UserSerializer, ItensSerializer, InventarioSerializer


class ItensApiView(APIView):
    def get(self, request):
        itens = Itens.objects.all()
        serializer = ItensSerializer(itens, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ItensSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)    

        

class UserApiView(APIView):
    def get(self, request):
        user = User.objects.all()
        serializer = UserSerializer(user, many=True)
        return Response(serializer.data)


class InventarioApiView(APIView):
    def get(self, request):
        inventario = Inventario.objects.all()
        serializer = InventarioSerializer(inventario, many=True)
        return Response(serializer.data)        


# Create your views here.
