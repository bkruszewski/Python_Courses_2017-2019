import pickle

baza = [
    ["Adam", "Kowalski", 34],
    ["Joanna", "Nowak", 48]
    ]

with open("baza.pkl", "wb") as plik:
    pickle.dump(baza, plik)
    print("zapisano")

    