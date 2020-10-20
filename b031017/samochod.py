class Samochod(object):
    def __init__(self, marka, model): #
        self.producent = marka # kazdy obiekt ma zmienne indwywidualne
        self.model = model  # moj obiekt bedzie mial zmienna model # kazdy obiekt ma zmienne indwywidualne
        self.czy_jedzie = None # kazdy obiekt ma zmienne indwywidualne

    def ruszaj(self):
        if self.czy_jedzie:
            print("Juz jedzie")
        else:
            self.czy_jedzie = True
            print("Ruszył")

    def trab(self, dlugosc):
        print(dlugosc * "i")

    def wypisz_info(self):
        print(f"Samochod: {self.producent} {self.model}")






