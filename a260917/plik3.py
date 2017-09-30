with open("dane") as plik:
    print(plik.tell()) # mowi w jakiej poyzcji sie znajdujemy
    linijka = plik.readline()
    print(linijka)
    print(plik.tell())
    znak = plik.read(1)
    print(znak)
    print(plik.tell())

    plik.seek(2)


