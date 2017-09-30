try:
    with open(dane.txt) as plik:
        print(plik.read())

except FileNotFoundError as e:
    print(e)
    print("Podany plik nie istnieje")

    raise ValueError("Bledna wartosc sciezki")

except Exception:
    print("Nieoczekiwany blad")

print("dalsza czesc programu")

