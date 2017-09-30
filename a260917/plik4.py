with open ("dane", "r+") as plik: # tryb a zostawia kursor na koncu linijki
    plik.write("Moja nowa dodana linia")
    plik.seek(1) # szuka 1 pozycji/ przesuwa się o 1??
    znak = plik.read(1) # Zczytuje kolejny znak
    print(znak)
    #
    # if znak == "\n":
    #     plik.write("Moja dopisana linijka")
    # else:
    #     plik.write("\nMoja dopisana linijka")
