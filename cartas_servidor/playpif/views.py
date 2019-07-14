from django.db.models import QuerySet
from django.db.transaction import atomic
from rest_framework import generics, permissions, status, viewsets, views
from rest_framework.response import Response

from playpif.models import Jogador, Carta, Sequencia
from playpif.serializers import JogadorSerializer, CartaSerializer, SequenciaSerializer


class JogadorView(generics.CreateAPIView):

    serializer_class = JogadorSerializer
    permission_classes = (permissions.AllowAny,)
    queryset = Jogador.objects.all()

    @atomic
    def post(self, request, *args, **kwargs):
        jogador_serializer = JogadorSerializer(data=request.data)
        if jogador_serializer.is_valid():
            jogador_serializer.save()
            return Response(jogador_serializer.data,
                            status=status.HTTP_201_CREATED)
        return Response(data={"error": "não foi possivel croncluir a operaçao"},
                        status=status.HTTP_400_BAD_REQUEST)


class CartaList(generics.ListAPIView):
    serializer_class = CartaSerializer
    queryset = Carta.objects.all()
    name = 'carta-list'


class CartaDetail(generics.RetrieveAPIView):
    serializer_class = CartaSerializer
    queryset = Carta.objects.all()
    name = 'carta-detail'


class SequenciaView(views.APIView):


    def post(self, request, *args, **kwargs):
        serializer = SequenciaSerializer(data=request.data)
        print(request.data)
        if serializer.is_valid():
            seq = serializer.create(serializer.validated_data)

        return Response(data={"validacao": "sequencia valida" if seq.validar() else "sequencia invalida"})
