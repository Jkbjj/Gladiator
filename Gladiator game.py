import random
import time
from random import randint


class Gracz:
    def __init__(self, imie, klasa):
        self.imie = imie
        self.klasa = klasa
        self.rozdzka = 0
        self.miecz = 5
        self.zbroja = 0
        self.kusza =  0
        self.statystyki = {"wygrane": 0, "przegrane": 0, "zdrowie" : 100, "kasa": 1000}
        if klasa == "Gladiator":
            self.statystyki.update({"moc": 7 + self.miecz, "zrecznosc": 5 + self.kusza,
            "inteligencja": 3 + self.rozdzka, "obrona":5 + self.zbroja})
        elif klasa == "Zwiadowca":
            self.statystyki.update({"moc": 3 + self.miecz, "zrecznosc": 7 + self.kusza,
            "inteligencja": 5 + self.rozdzka, "obrona": 5 + self.zbroja})
        elif klasa == "Mag":
            self.statystyki.update({"moc": 3 + self.miecz, "zrecznosc": 5 + self.kusza,
            "inteligencja": 7 + self.rozdzka, "obrona":5 + self.zbroja})
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
            self.statystyki['moc'] += 5 + random.randint(2, 4)
            self.statystyki['zrecznosc'] += 4 + random.randint(1, 3)
            self.statystyki['inteligencja'] += 3 +  random.randint(1, 4)
            self.statystyki['obrona'] += 4 + random.randint(1, 4)
class Boss():
    def __init__(self):
        self.statystyki = {"zdrowie": 300, "moc": 5, "zrecznosc": 4,"inteligencja": 3,"obrona": 3}
    def aktualizacja_statystyk_bossa(self, gracz):
        self.statystyki['zdrowie'] = round(gracz.statystyki['zdrowie'] * random.uniform(1.2,1.6))
        self.statystyki['moc'] = round(gracz.statystyki['moc'] * random.uniform(0.70,1.16))
        self.statystyki['zrecznosc'] = round(gracz.statystyki['zrecznosc'] * random.uniform(0.75,1.10))
        self.statystyki['inteligencja'] = round(gracz.statystyki['inteligencja'] * random.uniform(0.80,1.10))
        self.statystyki['obrona'] = round(gracz.statystyki['obrona'] * random.uniform(0.75,1.10))
class Rozdzka():
    def __init__(self, inteligencja):
        self.inteligencja = inteligencja

class Zbroja():
    def __init__(self, obrona):
        self.obrona = obrona
class Miecz():
    def __init__(self, moc):
        self.moc = moc
class Kusza():
    def __init__(self, zrecznosc):
        self.zrecznosc = zrecznosc


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
def menu(gracz, przeciwnik, boss):
    print("{} Witaj wśród Gladiatorów!".format(gracz.imie)," Twoja klasa to:",format(gracz.klasa) )
    print("arena - 1")
    print("sklep - 2")
    print("ekwipunek - 3")
    print("statystyki - 4")
    print("zakończ grę - 5")
    obsluga_menu(gracz, przeciwnik, boss)
# Funkcja obsługa menu nawiguje po menu i obsługuje mechanike poruszania się po menu
def obsluga_menu(gracz, przeciwnik, boss):
    while True:
        try:
            wybor = int(input("Gladiatorze: Jaką czynność chcesz wykonać? "))
            if wybor == 1:
                arena(gracz, przeciwnik, boss)
                break
            elif wybor == 2:
                sklep(gracz)
                break
            elif wybor == 3 :
                ekwipunek(gracz)
                break
            elif wybor == 4 :
                statystyki(gracz)
                break
            elif wybor == 5:
                print("Dziękuję za grę!")
                exit()
            else:
                print("Podano nieprawidłową wartość! Wybierz wartość od 1 do 5")
        except ValueError:
            print("Należy wprowadzić liczbę")

# Arena jest miejscem, gdzie toczą się walki. Korzysta ona z funkcji walka, aby wywołąć mechanikę walki
def arena(gracz, przeciwnik, boss):
    print("Witaj na arenie! Gdzie walka toczy się do ostatniej krwi")
    while True:
        decyzja = input("Czy chcesz podjąć walkę(tak/nie) ").lower()
        if decyzja == "tak" and (gracz.statystyki['wygrane'] % 5 != 0 or gracz.statystyki['wygrane'] == 0) :
            print("Walczysz z przeciwnikiem")
            walka(gracz, przeciwnik)
            break
        elif decyzja == "tak":
            print("Walczusz z bossem")
            boss.aktualizacja_statystyk_bossa(gracz)
            walka(gracz,boss)
            break
        elif decyzja == "nie":
            return
        else:
            print("Należy wybrac tak lub nie")
#Sklep będzie trzeba rozbudować na razie ejst to zarys
def sklep(gracz):
    while True:
        print("Witaj w sklepie! aby zobaczyć dostępny asortyment wejdz w wybraną kategorie")
        print("Rozdzki - 1")
        print("Miecze - 2")
        print("Zbroje - 3")
        print("Kusze - 4")
        print("Powrot do menu - 5")
        try:
            wybor = int(input("Wybieram: "))
            if wybor == 1:
                rozdzki(gracz)
            elif wybor == 2:
                miecze(gracz)
            elif wybor == 3:
                zbroje(gracz)
            elif wybor == 4:
                kusze(gracz)
            elif wybor == 5:
                break
            else:
                print("Podano nieprawidłową wartość! Wybierz wartość od 1 do 5")
        except ValueError:
            print("Należy wprowadzić liczbę")

def rozdzki(gracz):
    koszt_przedmiotow, wartosci_statystyk = generowanie_przedmiotow(gracz, Rozdzka, "inteligencja")
    zakup_przedmiotow(gracz,koszt_przedmiotow, wartosci_statystyk, "rozdzka" )
def miecze(gracz):
    koszt_przedmiotow, wartosci_statystyk = generowanie_przedmiotow(gracz, Miecz, "moc")
    zakup_przedmiotow(gracz,koszt_przedmiotow, wartosci_statystyk, "miecz" )
def zbroje(gracz):
    koszt_przedmiotow, wartosci_statystyk = generowanie_przedmiotow(gracz, Zbroja, "obrona")
    zakup_przedmiotow(gracz,koszt_przedmiotow, wartosci_statystyk, "zbroja" )
def kusze(gracz):
    koszt_przedmiotow, wartosci_statystyk = generowanie_przedmiotow(gracz, Kusza, "zrecznosc")
    zakup_przedmiotow(gracz,koszt_przedmiotow, wartosci_statystyk, "kusza" )

def generowanie_przedmiotow (gracz, klasa_przedmiotu, statystyka):
    print("Poniżej znajdują się statystyki przedmiotów")
    wartosci = [
        max(round(gracz.statystyki[statystyka] * 0.1 * random.uniform(0.8, 1.2)), 1),
        max(round(gracz.statystyki[statystyka] * 0.2 * random.uniform(0.8, 1.2)), 2),
        max(round(gracz.statystyki[statystyka] * 0.3 * random.uniform(0.8, 1.2)), 3)
    ]
    koszt_przedmiotow = []
    wartosci_statystyk = []
    for i, wartosc in enumerate(wartosci, start = 1):
        przedmiot = klasa_przedmiotu(wartosc)
        koszt = i * round(0.025 * gracz.statystyki['kasa'] * random.uniform(0.7,1.3))
        print(f" {klasa_przedmiotu.__name__}{i} - {statystyka} {wartosc} koszt {koszt} ")
        koszt_przedmiotow.append(koszt)
        wartosci_statystyk.append(wartosc)
    return  koszt_przedmiotow, wartosci_statystyk
def zakup_przedmiotow(gracz, koszt_przedmiotow , wartosci_statystyk, przedmiot):
    while True:
        try:
            wybor = int(input("Aby zakupić wybrany przedmiot wybierz (1-3). Aby wyjść klknij (4)  "))
            if wybor == 1:
                if gracz.statystyki["kasa"] < koszt_przedmiotow[0]:
                    print("Nie masz wystarczającej liczby pieniędzy")
                    break
                elif getattr(gracz, przedmiot) >= wartosci_statystyk[0]:
                    print("Masz już lepszy przedmiot")
                    break
                else:
                    setattr(gracz, przedmiot, wartosci_statystyk[0])
                    gracz.statystyki['kasa'] -= koszt_przedmiotow[0]
                    print("Gratulacje zakupiłeś przedmiot")
                    break
            elif wybor == 2:
                if gracz.statystyki["kasa"] < koszt_przedmiotow[1]:
                    print("Nie masz wystarczającej liczby pieniędzy")
                    break
                elif getattr(gracz, przedmiot) >= wartosci_statystyk[1]:
                    print("Masz już lepszy przedmiot")
                    break
                else:
                    setattr(gracz, przedmiot, wartosci_statystyk[1])
                    gracz.statystyki['kasa'] -= koszt_przedmiotow[1]
                    print("Gratulacje zakupiłeś przedmiot")
            elif wybor == 3:
                if gracz.statystyki["kasa"] < koszt_przedmiotow[2]:
                    print("Nie masz wystarczającej liczby pieniędzy")
                    break
                elif getattr(gracz, przedmiot) >= wartosci_statystyk[2]:
                    print("Masz już lepszy przedmiot")
                    break
                else:
                    setattr(gracz, przedmiot, wartosci_statystyk[2])
                    gracz.statystyki['kasa'] -= koszt_przedmiotow[2]
                    print("Gratulacje zakupiłeś przedmiot")
                    break
            elif wybor == 4:
                break
            else:
                print("Wybierz liczbę z zakresu 1-4")
        except ValueError:
            print("Należy wybrać wartość liczbową")


#ekwipunek będzie trzeba rozrysować
def ekwipunek(gracz):
    print("Poniżej znajduję się Twój ekwipunek")
    print(f" Rozdzka - inteligencja - {gracz.rozdzka}")
    print(f" Miecz - moc - {gracz.miecz}")
    print(f" Zbroja - obrona - {gracz.zbroja}")
    print(f" Kusza - zrecznosc - {gracz.kusza}")
    input("Aby powrócić do menu głównego kliknij dowolny klawisz: ")
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
            aktualizacja_statystyk_przeciwnika_po_walce(gracz, przeciwnik)
            time.sleep(2)
            regeneracja_zdrowia_wygrana(gracz)
            return
        time.sleep(2)
        atak_przeciwnika(gracz, przeciwnik)
        if gracz.statystyki['zdrowie'] <= 0:
            print("Zostałeś pokonany")
            przeciwnik.statystyki['zdrowie'] = 70
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

    obrazenia_przeciwnika = ((0.6 * moc) + (0.5 * zrecznosc) + (0.45 * inteligencja) -(0.6 * obrona)) * random.uniform(2, 3.35)
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
        print("Nie stać Ciebie na uleczenie!")
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
        print("Nie stać Ciebie na uleczenie. Game Over!")
        exit()
    else:
        gracz.statystyki['kasa'] -= koszt_uzdrowienie
        gracz.statystyki['zdrowie'] = 100
        print("Zostałeś wyleczony, z Twojego konta pobrano", koszt_uzdrowienie,"monet Twoje saldo to:", gracz.statystyki["kasa"])
        return
def aktualizacja_statystyk_przeciwnika_po_walce(gracz, przeciwnik):
    przeciwnik_to_boss = isinstance(przeciwnik, Boss)
    if przeciwnik_to_boss:
        return
    else:
        przeciwnik.aktualizacja_statystyk_przeciwnika(gracz)
        return





def main():
    przedmowa()
    klasa_gracza = klasa()
    imie_gracza = imie()
    gracz = Gracz(imie_gracza, klasa_gracza)
    przeciwnik = Przeciwnik()
    boss = Boss()
    while True:
        menu(gracz, przeciwnik, boss)
main()
