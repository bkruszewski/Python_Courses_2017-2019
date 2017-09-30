try:
    with open("lala") as file:
        print(file.read())

except FileNotFoundError as e:
    print("Nie znaleziono pliku", e)

except NameError:
    print("nie ma zmiennej")

except Exception:
    print("Pojawil sie nieoczekiwany blad")
