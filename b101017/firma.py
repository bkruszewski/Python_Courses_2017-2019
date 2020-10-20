from b101017.metody_klasy1 import Pracownik

prac1 = Pracownik("John", "aktor") # tworzymy instancje zeby uzyc metody
prac2 = Pracownik("Tom", "stara_gwiazda")


print(prac1)
print(prac2)

prac2.ustaw_pensje(10500)
print(prac2)

prac2.ustaw_roczna_podwyzka(50)
print(prac2)

prac1.pracownik_z_pensja("Kowalski", "Kelner", 3000)
print(prac1)


# prac2.daj_podwyzke(5)
# print(prac2)
#
# prac1.roczna_podw = 20 # wewnetrzna informacja dla obiektu prac2, ktora python nadpisuje
# print(prac1.roczna_podw)


# print ("\nIlosc pracownikow(klasa, obiekt1, obiekt2)")
# print(Pracownik.ilosc_pracownikow)
# print(prac1.ilosc_pracownikow)
# print(prac2.ilosc_pracownikow)
# #
# print("\n Roczna podwyzka(klasa, obiekt1, obiekt2)")
# print(Pracownik.roczna_podw)
# print(prac1.roczna_podw)
# print(prac2.roczna_podw)
#
# print ("Pracownik:")
# print(Pracownik.__dict__)
# print()
#
#
# print("osoba1")
# print(prac1.__dict__)
# print()
#
# print("prac:")
# print(prac2.__dict__)
# print()



