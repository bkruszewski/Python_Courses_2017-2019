from b051017.zwierze import Zwierze
from b051017.czlowiek import Czlowiek
from b051017.pies import Pies

#tworzymy zwierzaka

zwierz = Zwierze("Pimpuś")

zwierz.biega()
zwierz.halasuj()

# czlowiek

czlek = Czlowiek("Alojzy", 34)

czlek.halasuj()
czlek.biega()

psina = Pies("Azor")

psina.halasuj()

czlek.podaj_wiek()

