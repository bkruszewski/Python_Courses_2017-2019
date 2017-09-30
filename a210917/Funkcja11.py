#spr czy string jest palindrom
#docstring



from a210917.Funkcja7 import odwroc_str

def czy_palindrom(fraza:str):
    '''
    Sprawdza czy podana fraza jest palindromem
    :param fraza: zdanie do sprawdzenia
    :return: True jesli fraza jest palindromem
    '''
    for litera1, litera2 in zip(fraza, odwroc_str(fraza)):
        if litera1 != litera2:
            return False
        return True


print(czy_palindrom("kajak"))
print(czy_palindrom("bajka"))