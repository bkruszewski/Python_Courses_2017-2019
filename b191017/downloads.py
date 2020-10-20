import requests

def pobierz_foto(link, sciezka):

    response = requests.get(link)

    if response.status_code == 200:

        bajty = 0

        try:
            with open(sciezka, "wb") as plik:
                for part in response.iter_content(100000):
                    ilosc = plik.write(part)
                    bajty += ilosc

        except FileNotFoundError:
            #tutaj tworzymy folder
            print("Bajty")

        print(f"Zapisano {bajty} bajtow")

def main():
    link = "http://thumb7.shutterstock.com/display_pic_with_logo/2551714/423820774/stock-vector-smiley-faces-group-of-vector-emoticon-characters-with-funny-facial-expressions-d-realistic-vector-423820774.jpg"

    pobierz_foto(link, "smiley.jpg")

if __name__ == "__main__":
    main()
