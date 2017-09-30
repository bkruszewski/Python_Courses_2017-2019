osoby = {"studenci":["Ala", "Jan", "Ania"], "wykladowcy":["doktor", "profesor"]}
print(osoby["studenci"][1])
print(enumerate(osoby))



osoby["wykladowcy"].append("magister")
print(osoby)

osoby["administracja"] = ["pani Basia z dziekanatu"]
print(osoby)

osoby.update({"ochrona":"Impel"})
print(osoby)

print(osoby.keys)
print(osoby.values)

# for key, item in osoby():
# print(key, item)                 #Czemu to sie nie drukuje? Czy ta sie wydrukować key: item, key: item?



