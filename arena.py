import time
import random
from przeciwnik import Przeciwnik, Boss

def arena(gracz, przeciwnik, boss):
    print("Witaj na arenie! Gdzie walka toczy się do ostatniej krwi")
    while True:
        decyzja = input("Czy chcesz podjąć walkę(tak/nie) ").lower()
        if decyzja == "tak":
            if (gracz.statystyki['wygrane'] % 5 != 0 or gracz.statystyki['wygrane'] == 0):
                print("Walczysz z przeciwnikiem")
                walka(gracz, przeciwnik)
                break
            else:
                print("Walczusz z bossem")
                boss.aktualizacja_statystyk_bossa(gracz)
                walka(gracz,boss)
                break
        elif decyzja == "nie":
            return
        else:
            print("Należy wybrac tak lub nie")

def walka(gracz, przeciwnik):
    print("Rozpoczyna się walka do ostatniej krwi!")
    print(f"Twoje zdrowie: {gracz.statystyki['zdrowie']}, Zdrowie przeciwnika: {przeciwnik.statystyki['zdrowie']}")
    while przeciwnik.statystyki['zdrowie'] > 0 and gracz.statystyki['zdrowie'] >0 :
        atak_gracza(gracz, przeciwnik)
        if przeciwnik.statystyki['zdrowie'] <= 0:
            print("Gratulację, wygrałeś walkę")
            gracz.aktualizacja_statystyk_po_wygranej()
            aktualizacja_statystyk_przeciwnika_po_walce(gracz, przeciwnik)
            time.sleep(2)
            regeneracja_zdrowia(gracz,"Wygrana")
            return
        time.sleep(2)
        atak_przeciwnika(gracz, przeciwnik)
        if gracz.statystyki['zdrowie'] <= 0:
            print("Zostałeś pokonany")
            przeciwnik.statystyki['zdrowie'] = 0.7 * przeciwnik.statystyki['max_zdrowie']
            gracz.statystyki["przegrane"] += 1
            time.sleep(2)
            regeneracja_zdrowia(gracz,"Przegrana")
            return
        time.sleep(2)


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

def atak_gracza(gracz, przeciwnik):
    print("Wykonujesz atak")
    obrazenia = liczenie_obrazen(gracz,przeciwnik,gracz.klasa)
    przeciwnik.statystyki['zdrowie'] -= obrazenia
    print(f"Gracz zadaje {obrazenia} obrażeń. Zdrowie przeciwnika: {przeciwnik.statystyki['zdrowie']}")
    return obrazenia
def atak_przeciwnika(gracz, przeciwnik):
    print("Przeciwnik wykonuje atak")
    obrazenia = liczenie_obrazen(przeciwnik, gracz)
    gracz.statystyki['zdrowie'] -= obrazenia
    print(f"Przeciwnik zadaje {obrazenia} obrażeń. Zdrowie gracza: {gracz.statystyki['zdrowie']}")
    return obrazenia
def regeneracja_zdrowia(gracz, wynik):
    max_zdrowie = gracz.statystyki['max_zdrowie']
    if wynik == "Wygrana":
        if max_zdrowie == gracz.statystyki['zdrowie']:
            return
        koszt_uzdrowienie = random.randint(5, 25)
        print(f"Wygrałeś walkę, lecz ucierpoałeś, Twoje aktualne zdrowie wynosi {gracz.statystyki['zdrowie']}")
        print("Koszt Twojego uzdrowienia wynosi: ",koszt_uzdrowienie)
        if gracz.statystyki["kasa"] < koszt_uzdrowienie:
            print("Nie stać Ciebie na uleczenie!")
            return
        while True:
            decyzja = input("Czy chcesz zregenerować zdrowie? (tak/nie) ").lower()
            if decyzja == "tak":
                gracz.statystyki['kasa'] -= koszt_uzdrowienie
                gracz.statystyki['zdrowie'] = max_zdrowie
                print("Zostałeś wyleczony")
                break
            elif decyzja == "nie":
                print("Twoje zdrowie nie zostało zregenerowane")
                break
            else:
                print("Proszę wybrać tak lub nie")
    elif wynik == "Przegrana":
        koszt_uzdrowienie = random.randint(25, 75)
        if gracz.statystyki["kasa"] < koszt_uzdrowienie:
            print("Nie stać Ciebie na uleczenie. Game Over!")
            exit()
        else:
            gracz.statystyki['kasa'] -= koszt_uzdrowienie
            gracz.statystyki['zdrowie'] = max_zdrowie
            print("Zostałeś wyleczony, z Twojego konta pobrano", koszt_uzdrowienie, "monet Twoje saldo to:",
          gracz.statystyki["kasa"])
            return

def aktualizacja_statystyk_przeciwnika_po_walce(gracz, przeciwnik):
    przeciwnik_to_boss = isinstance(przeciwnik, Boss)
    if przeciwnik_to_boss:
        return
    else:
        przeciwnik.aktualizacja_statystyk_przeciwnika(gracz)
        return