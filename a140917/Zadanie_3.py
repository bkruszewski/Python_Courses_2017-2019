import string

litery = 0
cyfry = 0
male_lit = 0
duze_lit = 0

zdanie = input ("napisz cos: ")

for c in zdanie:
    if c.isdigit():
        cyfry +=1
    elif c.isalpha():
        litery +=1
        if c in string.ascii_lowercase:
            male_lit += 1
        else:
            duze_lit += 1
print(litery)
print(cyfry)
print (male_lit)
print (duze_lit)


