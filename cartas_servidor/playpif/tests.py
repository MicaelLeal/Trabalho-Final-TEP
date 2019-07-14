from django.test import TestCase


from playpif.models import Carta

def main():
    naipes = 'clubs hearts spades diamonds'.split()
    valores = 'ace king queen jack 10 9 8 7 6 5 4 3 2'.split()

    for n in naipes:
        for v in valores:
            Carta.objects.create(naipe=n, valor=v)
