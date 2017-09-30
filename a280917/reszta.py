monety = [5, 2, 1, 0.5, 0.2, 0.1]
wydac = [0, 0, 0, 0, 0, 0]

banknot = 20
zakup = 11.3
reszta = banknot - zakup
print(f" Do wydania: {reszta} zlotych")

for indeks, moneta in enumerate(monety):
    if reszta >= moneta:
        ilosc = reszta // moneta  # dzielenie cakowite
        wartosc = ilosc * moneta
        reszta = round(reszta - wartosc, 2)

        wydac[indeks] = ilosc
    # print(f"reszta: {reszta}, {wydac}")

print("Wydac:")
for moneta, ilosc in zip(monety, wydac):
    print (moneta," ", ilosc)