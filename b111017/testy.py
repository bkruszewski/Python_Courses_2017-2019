from unittest import TestCase
from b111017.zawodnik import Zawodnik

class TestZawodnik(TestCase): # kazda metoda testowa bedzie jednym testem

    def setUp(self): # utworzy obiekt przed kazdym testem
        self.zawodnik = Zawodnik("jan", "pilka")

    def test_init(self):

        self.assertEqual("jan", self.zawodnik.imie)

    def test_ustaw_nr_koszulki(self):

        self.zawodnik.ustaw_nr_koszulki(23)

        self.assertEqual(23, self.zawodnik.wypisz_numer())

    def test_zly_nr_koszulki(self):
        self.zawodnik.ustaw_nr_koszulki(150)
       # zmienna z oczekiwanym stringiem Zawodnik nie ma numeru
        self.assertIsNone(self.zawodnik.wypisz_numer())

#
