def dodaj_imie(imie, imiona=[]):
    imiona.append(imie.capitalize())
    return imiona

baza = ["ala"]

dodaj_imie("Ola", "Ala")
return dodaj_imie()



nowa_baza = dodaj_imie("Marta")
print(nowa_baza)
dodaj_imie("Marek", nowa_baza)
print(nowa_baza)

anglicy = dodaj_imie("Tommy")
print(anglicy)
