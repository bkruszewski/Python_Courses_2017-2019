#moja pierwsza zmienna
imie = "Ala"
print (imie)
print (3*imie)
nazwisko = "kowalska"
# print (imie + ' '+ nazwisko.capitalize())
print ('{} {}'.format(imie, nazwisko.capitalize()))
print ('{0} {1}'.format(imie, nazwisko.capitalize()))

nazwisko_duze = nazwisko.capitalize()

print ("Nazwisko z dużej:", nazwisko_duze)
print ("Nazwisko oryginalne:", nazwisko)
