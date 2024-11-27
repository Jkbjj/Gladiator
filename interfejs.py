import time
from arena import arena
from sklep import rozdzki, miecze, zbroje, kusze

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
def ekwipunek(gracz):
    print("Poniżej znajduję się Twój ekwipunek")
    print(f"Rozdzka - inteligencja - {gracz.rozdzka}\nMiecz - moc - {gracz.miecz}\n"
          f"Zbroja - obrona - {gracz.zbroja}\nKusza - zrecznosc - {gracz.kusza} ")
    input("Aby powrócić do menu głównego kliknij dowolny klawisz: ")
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
