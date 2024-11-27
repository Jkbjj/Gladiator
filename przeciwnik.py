import random
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