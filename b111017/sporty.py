from b111017.zawodnik import Zawodnik

z1 = Zawodnik("Lewy", "pilka nozna")

print(z1.imie)
print(z1.dyscyplina)
# print(z1.__numer_koszulki)

z1.ustaw_nr_koszulki(12)

z1.wypisz_numer()

z1.ustaw_zarobki("milion")
z1.wypisz_zarobki()
#
z1._Zawodnik__zarobki = 200  #czemu przed zawodnikiem jest podkreslnik?
print(z1._Zawodnik__zarobki)
