from b051017.czlowiek import Czlowiek

class Klient(Czlowiek):

    def __init__(self, imie, pesel):
        self.pesel = pesel

        wiek = str(pesel)[0:2]

        Czlowiek.__init__(self, imie, wiek)

    def wypozycz(self, film):
        film.klient = self    # odnosi sie tylko do filmu. Jesli nie bedzie pola klient w filmie to Python
                                # je utworzy

