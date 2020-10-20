class Pracownik(object):

    ilosc_pracownikow = 0 # zmienna klasy na poziomie klasy
    roczna_podw = 5

    def __init__(self, imie, stanowisko): # zmienne instancji
        self.imie = imie                    # tylko metody instancji maja dostep do obiektow
        self.stanowiko = stanowisko
        self.wynagrodzenie = None

        Pracownik.ilosc_pracownikow += 1# Jak wywoła funkcję to znaczy ze przybywa nam pracownika

    def ustaw_pensje(self, kwota):
        if kwota > 10000:
            self.wynagrodzenie = 10000
        else:
            self.wynagrodzenie = kwota

    def daj_podwyzke(self, procent):
        self.wynagrodzenie += self.wynagrodzenie * (procent/100)

    @classmethod # metoda klasy sluza do manipulacji zmiennymi na poziomie klasy i mozemy je wykorzystac do __init__
    def ustaw_roczna_podwyzka(cls, wartosc): # definiujemy obiekt klasy
        cls.roczna_podw = wartosc

    @classmethod # metoda dynamiczna
    def pracownik_z_pensja(cls, imie1, stanowisko1, pensja):

        prac = Pracownik(imie1, stanowisko1)
        prac.wynagrodzenie = pensja

        return prac

    @staticmethod # metoda statyczna / nie maja info z obiektów: czy tam metoda ma dostęp do zmiennych klasy?
    def sprawdz_pesel(pesel):

        if len(str(pesel)) == 11:
            return True
        else:
            return False

    def __str__(self):
        return f"{self.imie} - {self.stanowiko} ma pensje {self.wynagrodzenie}"