import random
from random import randint

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