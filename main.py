from interfejs import przedmowa, imie, klasa, menu, arena
from gracz import Gracz
from przeciwnik import Przeciwnik, Boss



def main():
    przedmowa()
    klasa_gracza = klasa()
    imie_gracza = imie()
    gracz = Gracz(imie_gracza, klasa_gracza)
    przeciwnik = Przeciwnik()
    boss = Boss()
    while True:
        menu(gracz, przeciwnik, boss)
if __name__ == "__main__":
    main()