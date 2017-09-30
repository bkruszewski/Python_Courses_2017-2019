#kolejka FIFO np. magazyn

kolejka = []

kolejka.append(1)
kolejka.append(56)
kolejka.append(23)

print(kolejka)

element = kolejka.pop(0) # usuwa 1 element
print(element)

print(kolejka)

kolejka.append(45)

kolejka.pop(0)
print(kolejka)

#LiFo
stos = [1, 2, 3, 4]
stos.append(87)
stos.append(854)
stos.append(567)

print(stos)

element2 = stos.pop() # usuwa ostatni element
print(element2)
print(stos)



