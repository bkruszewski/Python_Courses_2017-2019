# Sprawdz czy liczba jest podzielna przez 3, 5, 7

liczba = input("Podaj liczbe: ")

if liczba.isnumeric():
    liczba = int(liczba)

    if liczba % 3 == 0:
        print (f"Liczba {liczba} jest podzielna przez 3")
    if liczba % 5 == 0:  # wykona tylko jesli powyzszy warunek true
        print("Liczba jest podzielna przez 5")
    if liczba % 7 == 0:  # wykona tylko jesli powyzszy warunek true
        print("Liczba jest podzielna przez 7")


                # print ("to jest liczba:", liczba)
else:
    print("Podaj mi tylko liczbę!!!")

import this

