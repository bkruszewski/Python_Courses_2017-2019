from b051017.klient import Klient
from b051017.film import Film

kl1 = Klient("Adam", 897688473621)
kl2 = Klient("Joanna", 984574859438)

film1 = Film ("Rambo 3", 15.99)
film2 = Film("Polowanie na czerwony", 10)
film3 = Film("Narcos", 40)


kl1.wypozycz(film1)

print(film1)
print(film2)
print(film3)