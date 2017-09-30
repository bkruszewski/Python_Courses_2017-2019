#min 6 znaków, liczby i litery

haslo = input("podaj haslo")
prawidlowe = False

while not prawidlowe:
    if len(haslo) < 6:
        prawidlowe = False
        print ("Haslo za krótkie")
    else:
        prawidlowe = True

    if haslo.isalpha():
        print ("Haslo musi zawierać cyfry")
        prawidlowe = False
    else:
        prawidlowe = True

    if haslo.isnumeric():
        print("Haslo musi zawierać litery")
        prawidlowe = False
    else:
        prawidlowe = True

if not prawidlowe:
    haslo = input ("Podaj prawidlowe haslo")
    


#if prawidlowe = True
 #   print ("Haslo prawidlowe")

