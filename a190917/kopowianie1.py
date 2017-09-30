#kopowianie list z typami prostymi

wynik = 3

lista_a = ["zero", "jeden", wynik]
print ("lista a:", lista_a)

wynik = 43
lista_a = ["zero", "jeden", wynik]
print ("lista a:", lista_a)

lista_b = lista_a.copy()
print('lista_b:', lista_b)

lista_a.append("nowy")
print ("lista a:", lista_a)
print('lista_b:', lista_b)

print(hex(id(lista_a)))
print(hex(id(lista_b)))

