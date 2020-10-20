from b101017.animal import Animal

class Horse (Animal):
    def __init__(self, imie):
        Animal.__init__(self.imie)
        self.name = imie



    def say(self):
        print(f"{self.name} rzy")

    def jump(self):
        print(f"Kon {self.name} skacze")
