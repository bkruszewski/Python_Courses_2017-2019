with open ("dane", "r+") as plik:

    print(plik.tell())
    plik.read()
    poz = plik.tell()
    print(poz)
    #ustawiam na przedostatnia pozycje
    plik.seek(poz - 1)
    #
    znak = plik.read(1)
    print(znak)

    if znak == "\n":
        plik.write("Byl znak nowej linii\n")
    else:
        plik.write("\nNie było nowej linii")


