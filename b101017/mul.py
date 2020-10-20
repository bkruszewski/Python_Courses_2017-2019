from b101017.animal import Animal
from b101017.donkey import Donkey
from b101017.horse import Horse


class Mul(Donkey, Horse):
    def say(self):
        print("Mul mowi cos takiego")
        #super().say()
        Animal.say(self)

