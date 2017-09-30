with open ("dane", "w") as plik:
    print(plik.tell())

    s1 = "Ala ma kota"
    s2 = "Antoni gabka"
    s3 = "Policjanci z Miami\n"

    lista = [s1, s2, s3]
    print(lista)
    # plik.writelines(lista) # to zapisze stringi ciagiem

    plik.writelines([])

    plik.writelines([s+'\n' for s in lista ]) # co oznaczało s+'\n'
    