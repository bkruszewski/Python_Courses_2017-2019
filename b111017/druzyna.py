class Druzyna(object):

    def __init__(self, nazwa, trener):
        self.nazwa = nazwa
        self.trener = trener
        self.__budzet = None
        self.__transfery = []

    @property # getter - pobiera info z pola wyzej i oddaje - wrzucamy return
    def budzet(self):
        if self.__budzet is None:
            return "Brak budzetu"
        else:
            return self.__budzet

    @budzet.setter # sluzy do ustawiania wartosci zmiennej w kontrolowany sposob
    def budzet(self, wartosc):
        try:
            self.__budzet = int(wartosc)
        except:
            print("Podaj wartosc liczbowa")

    @property
    def transfery(self):
        if len(self.__transfery) == 0:
            return "brak transferow"
        else:
            return self.__transfery

    @transfery.setter
    def transfery(self, transfer):
        if isinstance(transfer, list):
            self.__transfery = transfer
        else:
            print("Podaj transfery jako liste")




