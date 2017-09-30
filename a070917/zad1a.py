# Sprawdz czy liczba jest podzielna przez 3 i 5 i 7

liczba = input("Podaj liczbe")

if liczba.isnumeric():
    liczba = int(liczba)
    if liczba % 3 == 0 and liczba % 5 == 0 and liczba % 7 == 0:
    print ("Liczba jest podzielna przez 3 i 5 i 7")

    else:
        print ("Liczba sie nie dzieli przez 3 i 5 i 7")



                # print ("to jest liczba:", liczba)
else:
    print("Podaj mi tylko liczbę!!!")
