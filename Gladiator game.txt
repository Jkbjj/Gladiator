import random
import time
from random import randint

#klasa gracz, jest odpowiedzialna za obiekt naszej postaci i zawiera potrzebne rzeczy do mechaniki gry

class Gracz:
    def __init__(self, imie, klasa):
        self.imie = imie
        self.klasa = klasa
        self.rozdzka = 0
        self.miecz = 0
        self.zbroja = 0
        self.kusza =  0
        self.statystyki = {"wygrane": 0, "przegrane": 0, "zdrowie" : 100, "kasa": 1000, "max_zdrowie": 100}
        if klasa == "Gladiator":
            self.statystyki.update({"moc": 7, "zrecznosc": 5,
            "inteligencja": 3, "obrona":5})
        elif klasa == "Zwiadowca":
            self.statystyki.update({"moc": 3, "zrecznosc": 7,
            "inteligencja": 5, "obrona": 5})
        elif klasa == "Mag":
            self.statystyki.update({"moc": 3, "zrecznosc": 5,
            "inteligencja": 7, "obrona": 5})

    def aktualizuj_statystyki(self):
        self.statystyki["moc"] += self.miecz
        self.statystyki["zrecznosc"] += self.kusza
        self.statystyki["inteligencja"] += self.rozdzka
        self.statystyki["obrona"] += self.zbroja
# aktualizacja statystyk po wygranej. Zlicza po walce wygrane przeciwnika i według zastosowanego wzoru oblicza statystyki
    def aktualizacja_statystyk_po_wygranej(self):
        self.statystyki["wygrane"] += 1
        self.statystyki["max_zdrowie"] += round((random.uniform(0.8, 1.3)* 10))
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

#klasa przeciwnik odpowada za rywali w podstawowej walce
class Przeciwnik:
    def __init__(self):
        self.statystyki = {"zdrowie": 40, "moc": 7, "zrecznosc": 4,"inteligencja": 4,"obrona": 4, "max_zdrowie": 100}
    def aktualizacja_statystyk_przeciwnika(self, gracz):
        self.statystyki["max_zdrowie"] += round((random.uniform(0.8, 1.3) * 10))
        if gracz.statystyki['wygrane'] % 3 != 0:
            self.statystyki['moc'] += random.randint(2, 4)
            self.statystyki['zrecznosc'] += random.randint(1, 3)
            self.statystyki['inteligencja'] +=  random.randint(1, 4)
            self.statystyki['obrona'] +=  random.randint(2, 4)
            self.statystyki['zdrowie'] = self.statystyki["max_zdrowie"]
        else:
            self.statystyki['moc'] += 5 + random.randint(2, 4)
            self.statystyki['zrecznosc'] += 4 + random.randint(1, 3)
            self.statystyki['inteligencja'] += 3 +  random.randint(1, 4)
            self.statystyki['obrona'] += 4 + random.randint(1, 4)
            self.statystyki['zdrowie'] = self.statystyki["max_zdrowie"]
#klasa Boss odpowiada za Bossa, którego gracz sotyka co 5 wyfrabych
class Boss():
    def __init__(self):
        self.statystyki = {"zdrowie": 300, "moc": 5, "zrecznosc": 4,"inteligencja": 3,"obrona": 3, "max_zdrowie": 300}
    def aktualizacja_statystyk_bossa(self, gracz):
        self.statystyki['max_zdrowie'] = round(gracz.statystyki['max_zdrowie'] * random.uniform(1.2,1.6))
        self.statystyki['zdrowie'] = self.statystyki['max_zdrowie']
        self.statystyki['moc'] = round(gracz.statystyki['moc'] * random.uniform(0.70,1.16))
        self.statystyki['zrecznosc'] = round(gracz.statystyki['zrecznosc'] * random.uniform(0.75,1.10))
        self.statystyki['inteligencja'] = round(gracz.statystyki['inteligencja'] * random.uniform(0.80,1.10))
        self.statystyki['obrona'] = round(gracz.statystyki['obrona'] * random.uniform(0.75,1.10))
#Rozdzka, Zbroja, Miecz i kusza odpowiadają, za przedmioty w grze


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
#Przedmowa wprowadza gracza w klimat gry
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
#Pytamy gracza o jego imię
def imie():
    imie = str(input("Gladiatorze witam! Podaj swoję imię!: "))
    return imie
#W funkcji klasa pytamy gracza o klasę jaką chcę wybrać. Wybór determinuje jego statystyki
def klasa():
    print("Graczu do wybooru są 3 klasy \nAby zostać: ")
    print("Dladiator kliknij - 1 \nZwiadowcą kliknij - 2 \nMagiem kliknij - 3")
    klasy = {1: "Gladiator", 2: "Zwiadowca", 3: "Mag"}
    while True:
        try:
            wybor = int(input("Mój wybór to: "))
            if wybor in klasy:
                print(f"Należysz do klasy {klasy[wybor].lower()}ów")
                return klasy[wybor]
            else:
                print("Wybierz liczbę z przedzaiłu 1-3 ")
        except:
            print("Nieprawidłowe danej wejściowe, wybierz liczbę  z przedziału 1-3 ")
# Funkcja menu zawiera ogólny zarys jest statyczna jej obsługa działa za pomocoś funkcji obsługa meny

MENU_OPCJE = {1: lambda gracz, przeciwnik, boss: arena(gracz,przeciwnik, boss),
              2: lambda gracz, przeciwnik=None, boss=None: sklep(gracz),
              3: lambda gracz, przeciwnik=None, boss=None:  ekwipunek(gracz),
              4: lambda gracz, przeciwnik=None, boss=None:  statystyki(gracz),
              5: lambda *_: exit()}
def menu(gracz, przeciwnik, boss):
    print("{} Witaj wśród Gladiatorów!".format(gracz.imie)," Twoja klasa to:",format(gracz.klasa) )
    print("1. Arena\n2. Sklep\n3. Ekwipunek\n4. Statystyki\n5. Zakończ grę")
    while True:
        try:
            wybor = int(input("Gladiatorze: Jaką czynność chcesz wykonać? "))
            if wybor in MENU_OPCJE:
                MENU_OPCJE[wybor](gracz, przeciwnik, boss)
                break
            else:
                print("Podano nieprawidłową wartość! Wybierz wartość od 1 do 5")
        except ValueError:
            print("Należy wprowadzić liczbę")
#Funkcja sklep ma za zadanie przenieść nas do przedmiotów, które chcemy kupić
def sklep(gracz):
    opcje = {1: lambda gracz: rozdzki(gracz), 2: lambda gracz: miecze(gracz),
             3: lambda gracz: zbroje(gracz), 4: lambda gracz: kusze(gracz)}
    while True:
        print("Witaj w sklepie! aby zobaczyć dostępny asortyment wejdz w wybraną kategorie")
        print("1. Rozdzki \n2. Miecze\n3. Zbroje\n4. kusze\n5. Powrót do menu")

        try:
            wybor = int(input("Wybieram: "))
            if wybor in opcje:
                opcje[wybor](gracz)
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
    #Generujemy statystyki różdzek według statystyk gracza
    wartosci = [
        max(round(gracz.statystyki[statystyka] * 0.1 * random.uniform(0.8, 1.2)), 1),
        max(round(gracz.statystyki[statystyka] * 0.2 * random.uniform(0.8, 1.2)), 2),
        max(round(gracz.statystyki[statystyka] * 0.3 * random.uniform(0.8, 1.2)), 3)
    ]
    koszt_przedmiotow = []
    wartosci_statystyk = []
    #Funkcja for liczy koszt dla każdej różdzki. Iteruję po i, więc 2 różdzka jest droższa od pierwszej
    #Funkcja wyświetla przedmioty ich statystykę i koszt. Oraz dołącza do list, z których gracz ją kupi
    for i, wartosc in enumerate(wartosci, start = 1):
        przedmiot = klasa_przedmiotu(wartosc)
        koszt = i * round(0.025 * gracz.statystyki['kasa'] * random.uniform(0.7,1.3))
        print(f" {klasa_przedmiotu.__name__}{i} - {statystyka} {wartosc} koszt {koszt} ")
        koszt_przedmiotow.append(koszt)
        wartosci_statystyk.append(wartosc)
    return  koszt_przedmiotow, wartosci_statystyk
def zakup_przedmiotow(gracz, koszt_przedmiotow , wartosci_statystyk, przedmiot):
#Funkcja zakup przedmiotów obsługuje decyzje gracza, co do zakupu. Sprawdza ksozt przedmiotu z saldem.
#Sprawdza wartość statystyk i porównuje ją z tymi posiadnaymi przez gracza
#Jeżeli warunki są spełnione umożliwia zakup
    while True:
        try:
            wybor = int(input("Aby zakupić wybrany przedmiot wybierz (1-3). Aby wyjść klknij (4)  "))
            if wybor in range (1,4):
                indeks = wybor - 1
                if gracz.statystyki["kasa"] < koszt_przedmiotow[indeks]:
                    print("Nie masz wystarczającej liczby pieniędzy")
                    time.sleep(2)
                    break
                elif getattr(gracz, przedmiot) >= wartosci_statystyk[indeks]:
                    print("Masz już lepszy przedmiot")
                    time.sleep(2)
                    break
                else:
                    setattr(gracz, przedmiot, wartosci_statystyk[indeks])
                    gracz.statystyki['kasa'] -= koszt_przedmiotow[indeks]
                    print("Gratulacje zakupiłeś przedmiot")
                    time.sleep(1)
                    gracz.aktualizuj_statystyki()
                    break
            elif wybor == 4:
                break
            else:
                print("Wybierz liczbę z zakresu 1-4")
        except ValueError:
            print("Należy wybrać wartość liczbową")
def ekwipunek(gracz):
    print("Poniżej znajduję się Twój ekwipunek")
    print(f"Rozdzka - inteligencja - {gracz.rozdzka}\nMiecz - moc - {gracz.miecz}\n"
          f"Zbroja - obrona - {gracz.zbroja}\nKusza - zrecznosc - {gracz.kusza} ")
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








