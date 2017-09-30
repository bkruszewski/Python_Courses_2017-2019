plik = open("dane")

linijka = plik.readline()
print(linijka)
linijka2 = plik.readline()
print(linijka2)

pozostaly_tekst = plik.read()
print(pozostaly_tekst)


plik.close()

