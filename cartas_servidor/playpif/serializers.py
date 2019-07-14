from django.contrib.auth.models import User
from django.db.models import QuerySet
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.validators import UniqueValidator

from playpif.models import Carta, Sequencia, Jogador


class JogadorSerializer(serializers.ModelSerializer):

    nickname = serializers.CharField(max_length=40)
    email = serializers.EmailField()
    password = serializers.CharField(min_length=3, write_only=True)

    class Meta:
        model = Jogador
        fields = ["nickname", "email", "password"]

    def validate(self, attrs):
        if 'nickname' not in attrs.keys():
            raise ValidationError('nickname is required')
        if 'email' not in attrs.keys():
            raise ValidationError('email is required')
        if 'password' not in attrs.keys():
            raise ValidationError('password is required')
        return attrs

    def create(self, data):
        usuario = User.objects.create_user(username=data['email'],
                                           email=data['email'],
                                           password=data['password'])
        return Jogador.objects.create(nickname=data['nickname'], usuario=usuario)


class CartaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Carta
        fields = '__all__'


class SequenciaSerializer(serializers.Serializer):

    carta1 = serializers.IntegerField()
    carta2 = serializers.IntegerField()
    carta3 = serializers.IntegerField()

    def validate(self, attrs):
        if ('carta1' or 'carta2' or 'carta3') not in attrs.keys():
            raise ValidationError('tres cartas são requeridas')
        return attrs

    def create(self, validated_data):
        seqs = Carta.objects.filter(id__in=[validated_data['carta1'],
                                            validated_data["carta2"],
                                            validated_data["carta3"]])
        print(len(seqs))
        return Sequencia(queryset=seqs)
