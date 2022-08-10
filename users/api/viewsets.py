from rest_framework import generics
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from ..models import User, Inventario, Itens
from ..serializers import ItensSerializer, InventarioSerializer, UserSerializer

class ItensApiView(generics.ListCreateAPIView):
    queryset = Itens.objects.all()
    serializer_class = ItensSerializer

class ItenApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Itens.objects.all()
    serializer_class = ItensSerializer


class UsersApiView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class InventariosApiView(generics.ListCreateAPIView):
    queryset = Inventario.objects.all()
    serializer_class = InventarioSerializer

class InventarioApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Inventario.objects.all()
    serializer_class = InventarioSerializer   

#API 2

class ItensViewSet(viewsets.ModelViewSet):
    queryset = Itens.objects.all()
    serializer_class = ItensSerializer  

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    @action(detail=True, methods=['get'])
    def inventario(self, request, pk=None):
        user = self.get_object()
        serializer = InventarioSerializer(user.inventario.all(), many=True)
        return Response(serializer.data)

class InventarioViewSet(viewsets.ModelViewSet):
    queryset = Inventario.objects.all()
    serializer_class = InventarioSerializer    