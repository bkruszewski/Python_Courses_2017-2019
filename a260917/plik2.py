plik = open("dane", "r")

print(plik.readline(), end="")

linijki = plik.readlines()
print(linijki)

plik.close()

