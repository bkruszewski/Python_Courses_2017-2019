class Zawodnik(object):

    def __init__(self, imie, dyscyplina):

        self.imie = imie
        self.dyscyplina = dyscyplina
        self.__zarobki = None
        self.__numer_koszulki = None


    def ustaw_nr_koszulki(self, numer):

        if numer > 0 and numer < 100:
            self.__numer_koszulki = numer
        else:
            print("Podaj prawidlowy numer koszulki!")

    @staticmethod
    def __sprawdz_numer(numer):
        if numer is None:
            return False
        else:
            return True

    def wypisz_numer(self):
        if Zawodnik.__sprawdz_numer(self.__numer_koszulki):
            return(self.__numer_koszulki)

        else:
            return(f"Zawodnik {self.imie} nie ma numeru")

    def ustaw_zarobki(self, kwota): # co to dokładnie to try robi? Sprawdza czy podana kwota jest intem?
        try:
            self.__zarobki= int(kwota)
        except:
            print("Zarobki musza byc podane cyfrowo")
            self.__zarobki = 0

    def wypisz_zarobki(self):
        if self.__zarobki == 0:
            print ("Brak info")
        elif self.__zarobki > 100000:
            print("Bardzo duzo")
        elif self.__zarobki > 10000:
            print ("Moze byc")
        else:
            print("slabo")

