def odwroc_str(zdanie):
     return zdanie [::-1]

def odwroc_input():
    zdanie = input("Podaj zdanie: ")
    return odwroc_str(zdanie)

def glowna():
    print(odwroc_str ("Stoł z powyloamywanymi nogami"))
    print(odwroc_input())

if __name__ == '__main__': # jesli kod uruchamiany bezposrednio to rowniez uruchom te czesc kodu
    glowna()


