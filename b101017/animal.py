class Animal(object):
    def __init__(self, imie):
        self.imie = imie

    def say(self):
        print(f"Zwierzak {self.imie} nie mowi")

    def capitalize_name(self):
        self.imie = self.imie.capitalize()

