# 8. podane 3 boki trojkata, okresl
#     - czy uda sie narysowac trojkata
#       * dl. jednego boku musi byc < dlugosc sumy dwoch pozostalych
#     - czy jest to tr. roznoboczny, rownoramienny czy rownoboczny

a = int(input("podaj dl. podstawy a: "))
b = int(input("podaj dl. boku b: "))
c = int(input("podaj dl. boku c: "))

if a < b + c:
    print("Trojkat namalowany")

    if a != b and a != c and b != c:
        print(" Trojkat roznoboczny")
    elif a == b and a == c and b == c:
        print("Trojkat rownoboczny")
    else:
        print (" Trojkat rownoramienny")

else:
    print ("Nie da sie narysowac trojkata ")




# if (a == b and c < a + b) or (a == c and b < a + c) or (c == b and a < c + b):
#     print("Trojkat rownoramienny")




