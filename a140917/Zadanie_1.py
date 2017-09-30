#min 6 znaków, liczby i litery

haslo = input("podaj haslo")

while len(haslo) < 6 and haslo.co:
    print("Hasło za krótkie")
    haslo = input ("Podaj haslo: ")

print ("Prawidłowe hasło")