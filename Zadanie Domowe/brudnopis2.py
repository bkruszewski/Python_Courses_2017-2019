# def give_squere(x):
#     return(x**2)
#
# x = give_squere(2)
#
# print(x)

# def dodaj_imie(imie, imiona=[]):
#     imiona.append(imie)
#     return imiona

def dodaj_imie(imie, imiona=None):
    if imiona == None:
        imiona = []
    imiona.append(imie)
    return imiona


print(dodaj_imie("Bolek"))
print(dodaj_imie("Tomek"))








