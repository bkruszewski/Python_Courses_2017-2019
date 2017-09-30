#Sprawdz czy liczba jest podzielna przez 3 i 5 i 7

liczba = input ("Podaj liczbe")

if liczba.isnumeric():
    liczba = int (liczba)
    if liczba % 3 == 0:
        if liczba % 5 == 0: # wykona tylko jesli powyzszy warunek true
            if liczba % 7 == 0: # wykona tylko jesli powyzszy warunek true
                print ("Liczba jest podzielna przez 3 i 5 i 7")


    #print ("to jest liczba:", liczba)
else:
    print ("Podaj mi tylko liczbę!!!")
