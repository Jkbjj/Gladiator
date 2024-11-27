import random
import time
from ekwipunek import Rozdzka, Miecz, Zbroja, Kusza
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