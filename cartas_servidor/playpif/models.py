from django.contrib.auth.models import User
from django.db import models


class Carta(models.Model):
    naipe = models.CharField(max_length=10)
    valor = models.CharField(max_length=2)

    @property
    def intValor(self):
        if self.valor == "ace":
            return 1
        if self.valor == "jack":
            return 11
        if self.valor == "queen":
            return 12
        if self.valor == "king":
            return 13
        return int(self.valor)

    def __str__(self):
        return "Carta: " + self.valor + ", " + self.naipe


class Sequencia:

    def __init__(self, queryset: models.QuerySet):
        self.cartas = queryset

    def validar(self):
        if len(self.cartas) != 3:
            return False
        return self.__isSequencia() or self.__isTrinca()

    def __isSequencia(self):
        naipes = self.getNaipes()
        if naipes[0] == naipes[1] == naipes[2]:
            valores = self.getValores()

            if valores[0] == 1 and valores[1] == 12 and valores[2] == 13:
                return True

            valores.sort()
            if valores[0] == valores[1] - 1 == valores[2] - 2:
                return True
        return False

    def __isTrinca(self):
        naipes = self.getNaipes()
        if naipes[0] != naipes[1] != naipes[2]:
            valores = self.getValores()
            return valores[0] == valores[1] == valores[2]
        return False

    def getNaipes(self):
        return [c.naipe for c in self.cartas.all()]

    def getValores(self):
        return [c.intValor for c in self.cartas.all()]


class Jogador(models.Model):
    nickname = models.CharField(max_length=40)
    usuario = models.OneToOneField(User, related_name="jogador",
                                   on_delete=models.CASCADE)

    @property
    def email(self):
        return self.usuario.email
