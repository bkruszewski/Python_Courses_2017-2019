from unittest import TestCase
from b171017.kalkulator import*
from b171017.helpers import *

class KalkTesty(TestCase):

    def setUP(self): # odpala sie przed kazdym testem np 2 testy to 2 razy sie odpala
        self.a = 10   # daje mi to ze nie musze wciaz powtarzac zmiennych
        self.b = 2


    def test_dodaj(self):  # kazda definicja funkcji testowej zaczyna sie od slowa test

        #arrange
        suma_oczekiwana = self.a + self.b

        #act
        suma_rzeczywista = dodaj(self.a, self.b)

        # assert
        self.assertEqual(suma_oczekiwana, suma_rzeczywista)

    def test_pomnoz(self):
        self.a = 10
        self.b = 2
        il_oczekiwany = self.a * self.b
        il_rzeczywisty = pomnoz(self.a,self.b)

        self.assertEqual(il_oczekiwany, il_rzeczywisty)

    def test_odejmij(self):
        wart_oczekiwana = self.a - self.b

        wart_rzeczywista = odejmij(self.a, self.b)

        self.assertEqual(wart_rzeczywista, wart_oczekiwana)
