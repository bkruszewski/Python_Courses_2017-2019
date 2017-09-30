imie = "jola"

def drukuj_imiona(imie_2):
    global imie             # odnosi sie do Jola- dostepne w calym kodzie

    imie = "ania".capitalize()
    imie_2 = imie_2.capitalize()

    print(imie, imie_2)

drukuj_imiona("gosia")
print(imie)

