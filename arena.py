import time
import random
from przeciwnik import Przeciwnik, Boss

class Walka():
    def __init__(self, gracz, przeciwnik):
        self.gracz = gracz
        self.przeciwnik = przeciwnik

    def fight (self):
        print("Rozpoczyna się walka do ostatniej krwi!")
        print(f"Twoje zdrowie: {self.gracz.statystyki['zdrowie']}, Zdrowie przeciwnika: {self.przeciwnik.statystyki['zdrowie']}")
        while self.przeciwnik.statystyki['zdrowie'] > 0 and self.gracz.statystyki['zdrowie'] >0 :
            self.atak_gracza()
            if self.przeciwnik.statystyki['zdrowie'] <= 0:
                print("Gratulację, wygrałeś walkę")
                self.gracz.aktualizacja_statystyk_po_wygranej()
                self.aktualizacja_statystyk_przeciwnika_po_walce()
                time.sleep(2)
                self.regeneracja_zdrowia("Wygrana")
                return
            time.sleep(2)
            self.atak_przeciwnika()
            if self.gracz.statystyki['zdrowie'] <= 0:
                print("Zostałeś pokonany")
                self.przeciwnik.statystyki['zdrowie'] = 0.7 * self.przeciwnik.statystyki['max_zdrowie']
                self.gracz.statystyki["przegrane"] += 1
                time.sleep(2)
                self.regeneracja_zdrowia("Przegrana")
                return
            time.sleep(2)
    def liczenie_obrazen(self,atakujacy, broniacy, klasa=None):
        return liczenie_obrazen(atakujacy, broniacy, klasa)
    def atak_gracza(self):
        print("Wykonujesz atak")
        obrazenia = self.liczenie_obrazen(self.gracz,self.przeciwnik, self.gracz.klasa)
        self.przeciwnik.statystyki['zdrowie'] -= obrazenia
        print(f"Gracz zadaje {obrazenia} obrażeń. Zdrowie przeciwnika: {self.przeciwnik.statystyki['zdrowie']}")
        return obrazenia
    def atak_przeciwnika(self):
        print("Przeciwnik wykonuje atak")
        obrazenia = self.liczenie_obrazen(self.przeciwnik, self.gracz)
        self.gracz.statystyki['zdrowie'] -= obrazenia
        print(f"Przeciwnik zadaje {obrazenia} obrażeń. Zdrowie gracza: {self.gracz.statystyki['zdrowie']}")

    def regeneracja_zdrowia(self, wynik):
        max_zdrowie = self.gracz.statystyki['max_zdrowie']
        if wynik == "Wygrana":
            if max_zdrowie == self.gracz.statystyki['zdrowie']:
                return
            koszt_uzdrowienie = random.randint(5, 25)
            print(f"Wygrałeś walkę, lecz ucierpoałeś, Twoje aktualne zdrowie wynosi {self.gracz.statystyki['zdrowie']}")
            print("Koszt Twojego uzdrowienia wynosi: ", koszt_uzdrowienie)
            if self.gracz.statystyki["kasa"] < koszt_uzdrowienie:
                print("Nie stać Ciebie na uleczenie!")
                return
            while True:
                decyzja = input("Czy chcesz zregenerować zdrowie? (tak/nie) ").lower()
                if decyzja == "tak":
                    self.gracz.statystyki['kasa'] -= koszt_uzdrowienie
                    self.gracz.statystyki['zdrowie'] = max_zdrowie
                    print("Zostałeś wyleczony")
                    break
                elif decyzja == "nie":
                    print("Twoje zdrowie nie zostało zregenerowane")
                    break
                else:
                    print("Proszę wybrać tak lub nie")
        elif wynik == "Przegrana":
            koszt_uzdrowienie = random.randint(25, 75)
            if self.gracz.statystyki["kasa"] < koszt_uzdrowienie:
                print("Nie stać Ciebie na uleczenie. Game Over!")
                exit()
            else:
                self.gracz.statystyki['kasa'] -= koszt_uzdrowienie
                self.gracz.statystyki['zdrowie'] = max_zdrowie
                print("Zostałeś wyleczony, z Twojego konta pobrano", koszt_uzdrowienie, "monet Twoje saldo to:",
                      self.gracz.statystyki["kasa"])
    def aktualizacja_statystyk_przeciwnika_po_walce(self):
        self.przeciwnik_to_boss = isinstance(self.przeciwnik, Boss)
        if self.przeciwnik_to_boss:
            return
        else:
            self.przeciwnik.aktualizacja_statystyk_przeciwnika(self.gracz)
            return
def liczenie_obrazen(atakujacy, broniacy, klasa=None):
    moc = atakujacy.statystyki["moc"]
    zrecznosc = atakujacy.statystyki["zrecznosc"]
    inteligencja = atakujacy.statystyki["inteligencja"]
    obrona = broniacy.statystyki["obrona"]
    if klasa == "Gladiator":
        wspolczynniki = {"moc": 0.7, "zrecznosc": 0.4, "inteligencja": 0.2, "obrona": 0.7}
        mnoznik = random.uniform(2, 3.5)
    elif klasa == "Zwiadowca":
        wspolczynniki = {"moc": 0.2, "zrecznosc": 0.7, "inteligencja": 0.4, "obrona": 0.7}
        mnoznik = random.uniform(2, 3.5)
    elif klasa == "Mag":
        wspolczynniki = {"moc": 0.2, "zrecznosc": 0.4, "inteligencja": 0.7, "obrona": 0.7}
        mnoznik = random.uniform(2, 3.5)
    else:  # Domyślny przypadek dla przeciwników
        wspolczynniki = {"moc": 0.6, "zrecznosc": 0.5, "inteligencja": 0.45, "obrona": 0.6}
        mnoznik = random.uniform(2, 3.35)
    obrazenia = (
        (wspolczynniki["moc"] * moc) +
        (wspolczynniki["zrecznosc"] * zrecznosc) +
        (wspolczynniki["inteligencja"] * inteligencja) -
        (wspolczynniki["obrona"] * obrona)
    ) * mnoznik
    return max(1, round(obrazenia))
