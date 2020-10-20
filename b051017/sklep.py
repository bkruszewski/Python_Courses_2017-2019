from b051017.przedmiot import Przedmiot

art1 = Przedmiot("Woda mineralna 1l", 2.30, 1)

polka_z_woda = []

for i in range (3):
    woda = Przedmiot ("Woda mineralna 1l", 2.30, 1)
    polka_z_woda.append(woda)



print(polka_z_woda[0:4])
# print(art1)
# polka = zip(polka_z_woda[0:3])
# print(polka) # jak wydrukować wszytkie instancje polka_z_woda w jednej liscie
#
#
# wartosc, ciezar = polka_z_woda[0] + polka_z_woda[1] # co dokladnie tutaj sumuje
#
# print(wartosc)
# print(ciezar)
#
#
# art2 = Przedmiot("chleb", 3.20, 0.5)
# print (art1 < art2)
#
#
# zakupy = art1 + art2
#
# print(f"Zakupy kosztuja: {zakupy[0]} i waza: {zakupy[1]}" )
#
# del art2
#
# print("------Koniec programu------")



