from b101017.metody_klasy1 import Pracownik

prac1 = Pracownik("John", "aktor")
prac2 = Pracownik("Tom", "stara_gwiazda")

print(prac1)
print(prac2)

prac2.ustaw_pensje(10500)
print(prac2)

prac2.daj_podwyzke(5)
print(prac2)

prac1.roczna_podw = 7 # wewnetrzna informacja dla obiektu prac2, ktora python nadpisuje i
# jest wazniejsza od tej ponizej nadanej przez klase

Pracownik.ustaw_roczna_podwyzka(12)

print(prac1.roczna_podw)
print(prac2.roczna_podw)

Pracownik.pracownik_z_pensja("Jan", "kamerzysta", 3000)

# print(type(prac3))

poprawny = Pracownik.sprawdz_pesel(123456789)
print(poprawny)


