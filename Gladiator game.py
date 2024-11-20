import random
import time

#zmienne są na razie jako globalne. Jak nauczę się klas tam je wrzucę
kasa = float(1000.00)
nazwagladiatora = ""
staty = {"moc": 5, "zręczność": 5,"inteligencja": 5,"obrona": 5, "zdrowie": 100}
statylevel1 = {"moc": 5, "zręczność": 4,"inteligencja": 4,"obrona": 4, "zdrowie": 40}
#Przedmowa na początku gry
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
    global nazwagladiatora
    nazwagladiatora = str(input("Gladiatorze witam! Podaj swoję imię!: "))
    return nazwagladiatora

# Funkcja menu zawiera ogólny zarys jest statyczna jej obsługa działa za pomocoś funkcji obsługa meny
def menu():
    print("{} Witaj wśród Gladiatorów!".format(nazwagladiatora))
    print("arena - 1")
    print("sklep - 2")
    print("ekwipunek - 3")
    print("statystyki - 4")
    print("saldo - 5")
    print("zakończ grę - 6")
    obsługa_menu()
# Funkcja obsługa menu nawiguje po menu i obsługuje mechanike poruszania się po menu
def obsługa_menu():
    while True:
        try:
            wybor = int(input("Gladiatorze: Jaką czynność chcesz wykonać? "))
            if wybor == 1:
                arena()
                break
            elif wybor == 2:
                sklep()
                break
            elif wybor == 3 :
                ekwipunek()
                break
            elif wybor == 4 :
                statystyki()
                break
            elif wybor == 5 :
                saldo()
                break
            elif wybor == 6:
                print("Dziękuję za grę!")
                exit()
            else:
                print("Podano nieprawidłową wartość! Wybierz wartość od 1 do 6")
        except ValueError:
            print("Należy wprowadzić liczbę")

# Arena jest miejscem, gdzie toczą się walki. Korzysta ona z funkcji walka, aby wywołąć mechanikę walki
def arena():
    print("Witaj na arenie! Gdzie walka toczy się do ostatniej krwi")
    while True:
        decyzja = input("Czy chcesz podjąć walkę(tak/nie) ").lower()
        if decyzja == "tak":
            walka(staty,statylevel1)
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
def statystyki():
    global staty
    print("Poniżej znajdują się Twoje statystyki")
    for stat, value in staty.items():
        print(f"{stat} - {value}")
    powrot1 = input("Aby powrócić do menu głównego kliknij dowolny klawisz: ")
#Saldo na razie ma funkcjonalność statyczną, będzie rozbudowane z rozwojem gry
def saldo():
    global kasa
    print("Poniżej znajdują się Twoje saldo: ")
    print("Twoje saldo to: ",kasa)
    powrot1 = input("Aby powrócić do menu głównego kliknij dowolny klawisz: ")
#Funkcja policz obrazenia jest kluczowa w imitacji walki
def policz_obrazenia(gracz, przeciwnik):
    moc = gracz["moc"]
    zrecznosć = gracz["zręczność"]
    inteligencja = gracz["inteligencja"]
    obrona = przeciwnik["obrona"]
    obrazenia = ((0.7 * moc) + (0.3 * zrecznosć) + (0.3 * inteligencja) - (0.6 * obrona)) * random.uniform(2,3.5)
    return max(1, round(obrazenia))
#walka imituje walkę, rozważyć podzielenie ruchów gracza i przeciwnika na dwie funkcje i wsadzenie jej do walki

def walka(gracz, przeciwnik):
    print("Rozpoczyna się walka do ostatniej krwi!")
    print(f"Twoje zdrowie: {gracz['zdrowie']}, Zdrowie przeciwnika: {przeciwnik['zdrowie']}")
    przeciwnik_zdrowie = przeciwnik["zdrowie"]
    gracz_zdrowie = gracz["zdrowie"]

    while gracz_zdrowie > 0 and przeciwnik_zdrowie >0 :
        print("Wykonujesz atak")
        obrazenia_gracza = policz_obrazenia(gracz,przeciwnik)
        przeciwnik_zdrowie -= obrazenia_gracza
        print(f"Gracz zadaje {obrazenia_gracza} obrażeń. Zdrowie przeciwnika: {przeciwnik_zdrowie}")
        if przeciwnik_zdrowie <= 0:
            print("Gratulację, wygrałeś walkę")
            time.sleep(2)
            return
        time.sleep(2)
        print("Przeciwnik wykonuje atak")
        obrazenia_przeciwnika = policz_obrazenia(przeciwnik, gracz)
        gracz_zdrowie -= obrazenia_przeciwnika
        print(f"Przeciwnik zadaje {obrazenia_przeciwnika} obrażeń. Zdrowie gladiatora: {gracz_zdrowie}")
        if gracz_zdrowie <= 0:
            print("Zostałeś pokonany")
            time.sleep(2)
            return
        time.sleep(2)

def main():
    przedmowa()
    imie()
    while True:
        menu()
main()




