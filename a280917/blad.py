import os

sciezka = "lala"

if os.path.exists(sciezka):
    with open(sciezka) as plik:
        zawartosc = plik.read()
        print(zawartosc)
else:
    print("plik nie istnieje")

    