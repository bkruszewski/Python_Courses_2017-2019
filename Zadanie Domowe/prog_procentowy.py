# 4. oblicz ocenę na podstawie progu procentowego

procenty = int(input("napisz ile procent dostales: "))

if procenty > 90:
    print("Ocena bardzo dobra")

elif 80 < procenty < 90:
    print("Ocena dobra")

elif 70 < procenty < 80:
    print("Ocena dosc dobra")

elif 60 < procenty < 70:
    print("Ocena dostateczna")

else:
    print("Niestety nie udalo sie")
