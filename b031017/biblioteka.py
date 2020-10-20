from b031017.ksiazka import Ksiazka

ks1 = Ksiazka("Brzechwa", "Lokomotywa")
ks2 = Ksiazka ("Forsyth", "Akta Odessy")

ks1.wypozycz()

print(f"ksiazka {ks1.tytul} wypozyczona {ks1.wypozyczona}")
print(f"ksiazka {ks2.tytul} wypozyczona {ks2.wypozyczona}")

print()
print(ks1)
print(ks2)
