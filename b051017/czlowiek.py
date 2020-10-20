from b051017.zwierze import Zwierze

class Czlowiek(Zwierze):

    def __init__(self, imie, wiek):
        self.imie = imie
        self.wiek = wiek

        Zwierze.__init__(self, imie) # inicjalizuje zwierze i juz nie musialbym
        #imienia czlowieka inicjalizowac ale wtedy musialbym podac konkretny argument

    def biega(self):
        print (f"Czlowiek {self.imie} biega")

    def halasuj(self):
        print(f"{self.imie} mowi \"Dzien dobry \"")

    def podaj_wiek(self):
        print(f"{self.imie} ma {self.wiek} lat")

