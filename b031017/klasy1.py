from b031017.samochod import Samochod

auto = Samochod("Volvo", "V40")
print(type(auto))

print(auto.model)
print(auto.producent)
print(auto.czy_jedzie)

auto.czy_jedzie = True

print(auto.czy_jedzie)

auto2 = Samochod("Fiat", "125p")

print(auto2.producent)
print(auto2.model)

auto2.czy_jedzie = "jedzie"

print(auto2.czy_jedzie)

