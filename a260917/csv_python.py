baza = []

with open ("osoby.csv", "r+") as plik:

    #lista kolumn - opis
    # opis = plik.read()
    # print(opis)
    # opis = opis.strip()
#
    for linijka in plik:
        #usuwamy whitespace
        linijka = linijka.strip()
        # lista elementow w linijce
        osoba= linijka.split(",")
        # print(osoba)
        baza.append(osoba)
        print(osoba)
        # print(baza)
        # baza.append(osoba)
# #
#     baza.append((["Jan", "Kowalski", "47"]))
#     print(baza)
#
#     dane_zapis = []
#     for osoba in baza:
#         osoba = ",".join(osoba)
#         dane_zapis.append(osoba + '\n')
#
#     plik.seek(0)
#     plik.writelines(dane_zapis)
#
# print(baza)

