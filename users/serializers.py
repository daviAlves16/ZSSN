from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
from .models import User, Itens, Inventario

class ItensSerializer(serializers.ModelSerializer):
    class Meta:
        model = Itens
        fields = (
            'id_itens',
            'nome',
            'pontos'
        )

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            'id_users',
            'nome',
            'sexo',
            'latitude',
            'longitude',
            'contaminacao'
        )


class InventarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventario
        fields = (
            'user',
            'item',
            'quantidade',
        )