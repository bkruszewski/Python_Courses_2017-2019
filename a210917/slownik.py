osoby = {"Ania ": "Kowalska", 2 : 234.4, "92": 4}

liczby = {1:2, 2:3, 3:4}
print (liczby[1])

#osoby = dict ()
print(osoby[2])

osoby["Joanna"] = "policja"
print(osoby)

osoby ["Joanna"] = "straż"
print(osoby)

print(osoby.keys())
print(osoby.values())

for key, value in osoby.items():
    print(f"klucz {key} - wartość: {value}")


