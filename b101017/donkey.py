from b101017.animal import Animal

class Donkey(Animal):
    def __init__(self, imie):
        self.name = imie

    def say(self):
        print(f"{self.name} rzy")

    def run(self):
        print(f"Kon {self.name} biegnie")
