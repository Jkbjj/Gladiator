import random
import time
from random import randint


class Gracz:
    def __init__(self, imie, klasa):
        self.imie = imie
        self.klasa = klasa
        self.statystyki = {"wygrane": 0, "przegrane": 0, "zdrowie" : 100, "kasa": 1000}
        if klasa == "Gladiator":
            self.statystyki.update({"moc": 7, "zrecznosc": 5, "inteligencja": 3, "obrona":5})
        elif klasa == "Zwiadowca":
            self.statystyki.update({"moc": 3, "zrecznosc": 7, "inteligencja": 5, "obrona": 5})
        elif klasa == "Mag":
            self.statystyki.update({"moc": 3, "zrecznosc": 5, "inteligencja": 7, "obrona":5})
    def aktualizacja_statystyk_po_wygranej(self):
        self.statystyki["wygrane"] += 1
        self.statystyki['kasa'] += randint(10,35)
        if self.klasa == "Gladiator":
            self.statystyki['moc'] += 2 + random.randint(3,5)
            self.statystyki['zrecznosc'] += 1 + random.randint(1,3)
            self.statystyki['inteligencja'] += random.randint(1,3)
            self.statystyki['obrona'] += 1 + random.randint(3,5)
        elif self.klasa == "Zwiadowca":
            self.statystyki['moc'] += random.randint(1,3)
            self.statystyki['zrecznosc'] += 2 + random.randint(3,5)
            self.statystyki['inteligencja'] += 1 + random.randint(2,4)
            self.statystyki['obrona'] += 1 + random.randint(3,5)
        elif self.klasa == "Mag":
            self.statystyki['moc'] += random.randint(1,3)
            self.statystyki['zrecznosc'] += 1 + random.randint(2,4)
            self.statystyki['inteligencja'] += 2 + random.randint(3,5)
            self.statystyki['obrona'] += random.randint(2,4)

class Przeciwnik:
    def __init__(self):
        self.statystyki = {"zdrowie": 40, "moc": 7, "zrecznosc": 4,"inteligencja": 4,"obrona": 4,}
    def aktualizacja_statystyk_przeciwnika(self, gracz):
        if gracz.statystyki['wygrane'] % 3 != 0:
            self.statystyki['zdrowie'] = 100
            self.statystyki['moc'] += random.randint(2, 4)
            self.statystyki['zrecznosc'] += random.randint(1, 3)
            self.statystyki['inteligencja'] +=  random.randint(1, 4)
            self.statystyki['obrona'] +=  random.randint(2, 4)
        else:
            self.statystyki['zdrowie'] = 100
            self.statystyki['moc'] += 4 + random.randint(2, 4)
            self.statystyki['zrecznosc'] += 4 + random.randint(1, 3)
            self.statystyki['inteligencja'] += 3 +  random.randint(1, 4)
            self.statystyki['obrona'] += 3 + random.randint(1, 4)



def przedmowa():
    print("Witaj w grze Gladiator, gdzie odwaga i spryt to klucz do chwały na arenie.")
    print("Wejdź w świat starożytnego Rzymu, gdzie każdy krok i decyzja mogą zdecydować o twoim triumfie lub upadku.")
    print("Przygotuj się na ekscytujące wyzwania, rywalizację o honor i zasłużoną sławę!")
    decyzja = input("Czy chesz zagrać? (tak/nie): ")
    if decyzja.lower() == "tak":
        return True
    else:
        print("Może następnym razem będziesz mieć więcej odwagi")
        exit()

#Gladiator podaje mi swoje imię
def imie():
    nazwa_gladiatora = str(input("Gladiatorze witam! Podaj swoję imię!: "))
    return nazwa_gladiatora
#Mechanika klas będzie stworzona później
def klasa():
    print("Graczu do wybooru są 3 klasy")
    print("Jeżeli chcesz zostać gladiatorem kliknij - 1")
    print("Jeżeli chcesz zostać zwiadowcą kliknij - 2")
    print("Jeżeli chcesz zostać magiem kliknij - 3")
    while True:
        try:
            wybor = int(input("Mój wybór to: "))
            if wybor == 1:
                print("Zostałeś gladiatorem")
                return "Gladiator"
            elif wybor == 2:
                print("Zostałeś zwiadowcą")
                return "Zwiadowca"
            elif wybor == 3:
                print("Zostałeś magiem")
                return "Mag"
            else:
                print("Wybierz liczbę z przedzaiłu 1-3 ")
        except:
            print("Nieprawidłowe danej wejściowe, wybierz liczbę  z przedziału 1-3 ")

# Funkcja menu zawiera ogólny zarys jest statyczna jej obsługa działa za pomocoś funkcji obsługa meny
def menu(gracz, przeciwnik):
    print("{} Witaj wśród Gladiatorów!".format(gracz.imie)," Twoja klasa to:",format(gracz.klasa) )
    print("arena - 1")
    print("sklep - 2")
    print("ekwipunek - 3")
    print("statystyki - 4")
    print("saldo - 5")
    print("zakończ grę - 6")
    obsluga_menu(gracz, przeciwnik)
# Funkcja obsługa menu nawiguje po menu i obsługuje mechanike poruszania się po menu
def obsluga_menu(gracz, przeciwnik):
    while True:
        try:
            wybor = int(input("Gladiatorze: Jaką czynność chcesz wykonać? "))
            if wybor == 1:
                arena(gracz, przeciwnik)
                break
            elif wybor == 2:
                sklep()
                break
            elif wybor == 3 :
                ekwipunek()
                break
            elif wybor == 4 :
                statystyki(gracz)
                break
            elif wybor == 5 :
                saldo(gracz)
                break
            elif wybor == 6:
                print("Dziękuję za grę!")
                exit()
            else:
                print("Podano nieprawidłową wartość! Wybierz wartość od 1 do 6")
        except ValueError:
            print("Należy wprowadzić liczbę")

# Arena jest miejscem, gdzie toczą się walki. Korzysta ona z funkcji walka, aby wywołąć mechanikę walki
def arena(gracz, przeciwnik):
    print("Witaj na arenie! Gdzie walka toczy się do ostatniej krwi")
    while True:
        decyzja = input("Czy chcesz podjąć walkę(tak/nie) ").lower()
        if decyzja == "tak":
            walka(gracz,przeciwnik)
            break
        elif decyzja == "nie":
            return
        else:
            print("Należy wybrac tak lub nie")
#Sklep będzie trzeba rozbudować na razie ejst to zarys
def sklep():
    print("Witaj w sklepie! z poniższego menu możesz wybrać co chcesz zakupić")
#ekwipunek będzie trzeba rozrysować
def ekwipunek():
    print("Poniżej znajduję się Twój ekwipunek")
#Statystyki, pokazują aktualne staty gracza, po stworzeniu klas będzie trzeba ją zmodyfikować
def statystyki(gracz):
    print("Poniżej znajdują się Twoje statystyki")
    for stat, value in gracz.statystyki.items():
        print(f"{stat} - {value}")
    input("Aby powrócić do menu głównego kliknij dowolny klawisz: ")
#Saldo na razie ma funkcjonalność statyczną, będzie rozbudowane z rozwojem gry
def saldo(gracz):
    print("Poniżej znajdują się Twoje saldo: ")
    print("Twoje saldo to: ",gracz.statystyki["kasa"])
    input("Aby powrócić do menu głównego kliknij dowolny klawisz: ")

#walka imituje walkę, rozważyć podzielenie ruchów gracza i przeciwnika na dwie funkcje i wsadzenie jej do walki
def walka(gracz, przeciwnik):
    print("Rozpoczyna się walka do ostatniej krwi!")
    print(f"Twoje zdrowie: {gracz.statystyki['zdrowie']}, Zdrowie przeciwnika: {przeciwnik.statystyki['zdrowie']}")
    while przeciwnik.statystyki['zdrowie'] > 0 and gracz.statystyki['zdrowie'] >0 :
        atak_gracza(gracz, przeciwnik)
        if przeciwnik.statystyki['zdrowie'] <= 0:
            print("Gratulację, wygrałeś walkę")
            gracz.aktualizacja_statystyk_po_wygranej()
            przeciwnik.aktualizacja_statystyk_przeciwnika(gracz)
            time.sleep(2)
            regeneracja_zdrowia_wygrana(gracz)
            return
        time.sleep(2)
        atak_przeciwnika(gracz, przeciwnik)
        if gracz.statystyki['zdrowie'] <= 0:
            print("Zostałeś pokonany")
            gracz.statystyki["przegrane"] += 1
            time.sleep(2)
            regeneracja_zdrowia_przegrana(gracz)
            return
        time.sleep(2)

def liczenie_obrazen_gracza (gracz,przeciwnik):
    moc = gracz.statystyki["moc"]
    zrecznosc = gracz.statystyki["zrecznosc"]
    inteligencja = gracz.statystyki["inteligencja"]
    obrona = przeciwnik.statystyki["obrona"]

    if gracz.klasa == "Gladiator":
        obrazenia = ((0.7 * moc) + (0.4 * zrecznosc) + (0.2 * inteligencja) -(0.7 * obrona)) * random.uniform(2, 3.5)
        return max(1, round(obrazenia))
    elif gracz.klasa == "Zwiadowca":
        obrazenia = ((0.2 * moc) + (0.7 * zrecznosc) + (0.4 * inteligencja) -(0.7 * obrona)) * random.uniform(2, 3.5)
        return max(1, round(obrazenia))
    elif gracz.klasa == "Mag":
        obrazenia = ((0.2 * moc) + (0.4 * zrecznosc) + (0.7 * inteligencja) -(0.7 * obrona)) * random.uniform(2, 3.5)
        return max(1, round(obrazenia))
def liczenie_obrazen_przeciwnika (gracz,przeciwnik):
    moc = przeciwnik.statystyki["moc"]
    zrecznosc = przeciwnik.statystyki["zrecznosc"]
    inteligencja = przeciwnik.statystyki["inteligencja"]
    obrona = gracz.statystyki["obrona"]

    obrazenia_przeciwnika = ((0.4 * moc) + (0.4 * zrecznosc) + (0.4 * inteligencja) -(0.6 * obrona)) * random.uniform(2, 3.25)
    return max(1, round(obrazenia_przeciwnika))
def atak_gracza(gracz, przeciwnik):
    print("Wykonujesz atak")
    obrazenia = liczenie_obrazen_gracza(gracz,przeciwnik)
    przeciwnik.statystyki['zdrowie'] -= obrazenia
    print(f"Gracz zadaje {obrazenia} obrażeń. Zdrowie przeciwnika: {przeciwnik.statystyki['zdrowie']}")
    return obrazenia
def atak_przeciwnika(gracz, przeciwnik):
    print("Przeciwnik wykonuje atak")
    obrazenia = liczenie_obrazen_przeciwnika(gracz, przeciwnik)
    gracz.statystyki['zdrowie'] -= obrazenia
    print(f"Przeciwnik zadaje {obrazenia} obrażeń. Zdrowie gracza: {gracz.statystyki['zdrowie']}")
    return obrazenia
def regeneracja_zdrowia_wygrana(gracz):
    koszt_uzdrowienie = random.randint(5,25)
    if gracz.statystyki['zdrowie'] == 100:
        print("Twoje zdrowie jest pełne nie musisz się leczyc! Gratulacje")
        return

    print(f"Wygrałeś walkę, lecz ucierpoałeś, Twoje aktualne zdrowie wynosi {gracz.statystyki['zdrowie']}")
    print("Koszt Twojego uzdrowienia wynosi: ",koszt_uzdrowienie)
    if gracz.statystyki["kasa"] < koszt_uzdrowienie:
        print("Nie stać Ciebie na uleczenie. Sprzedaj coś ze swojego ekwipunku i wylecz się w zakładce saldo!")
        return
    while True:
        decyzja = input("Czy chcesz zregenerować zdrowie? (tak/nie) ").lower()
        if decyzja == "tak":
            gracz.statystyki['kasa'] -= koszt_uzdrowienie
            gracz.statystyki['zdrowie'] = 100
            print("Zostałeś wyleczon")
            break
        elif decyzja == "nie":
            print("Twoje zdrowie nie zostało zregenerowane")
            break
        else:
            print("Proszę wybrać tak lub nie")

def regeneracja_zdrowia_przegrana(gracz):
    koszt_uzdrowienie = random.randint(25, 50)
    print("Przegrałeś walkę, Twoje zdrowie spadło do 0")
    if gracz.statystyki["kasa"] < koszt_uzdrowienie:
        print("Nie stać Ciebie na uleczenie. Sprzedaj coś ze swojego ekwipunku i wylecz się w zakładce saldo!")
        return
    else:
        gracz.statystyki['kasa'] -= koszt_uzdrowienie
        gracz.statystyki['zdrowie'] = 100
        print("Zostałeś wyleczony, z Twojego konta pobrano", koszt_uzdrowienie,"monet Twoje saldo to:", gracz.statystyki["kasa"])
        return





def main():
    przedmowa()
    klasa_gracza = klasa()
    imie_gracza = imie()
    gracz = Gracz(imie_gracza, klasa_gracza)
    przeciwnik = Przeciwnik()
    while True:
        menu(gracz, przeciwnik)
main()
