def wypisz_dane(imie, nazwisko, kurs = "Python", il_dni = 15):
    print(imie, nazwisko, kurs, il_dni)

wypisz_dane("Bolek", "Kruszewski")
wypisz_dane("Bolek", "Kruszewski", "Java")
wypisz_dane("Jan", "Matejko", "malarstwo", 3567)

wypisz_dane("Paulina", "K", 30)

wypisz_dane("Marek", "0", il_dni=25)

wypisz_dane(kurs="JavaScript", imie="Olaf", il_dni=34, nazwisko="Pierdziel")
