a = 0
b = 1
c = a + b
print(a)
print(b)
print(c)

while c < 100:
        a = b + c
        b = a + c
        c = b + a

        if a > 100 or b > 100 or c > 100:
            break

        print (a)
        print (b)
        print (c)
















# lista1 = list(range(0, 10))
# lista2 = []
#
# lista3 = [((x-2)+(x-1)) for x in lista1]
# print (lista3)







