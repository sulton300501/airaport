class Aeroport:
    def __init__(self, nomi, manzili):
        self.nomi = nomi
        self.manzili = manzili
        self.aviakompaniyalar = []

    def qoshish(self, aviakompaniya):
        self.aviakompaniyalar.append(aviakompaniya)

 

    
    def chiqar(self):
        print(f"{self.nomi} Aeroportining aviakompaniyalari:")
        for aviakompaniya in self.aviakompaniyalar:
            print(aviakompaniya)

class Aviakompaniya:
    def __init__(self, nomi, founded_year):
        self.nomi = nomi
        self.founded_year = founded_year

    def __str__(self):
        return f"{self.nomi} ({self.founded_year}-yilda o'z faoliyatini boshladi)"




aeroport1 = Aeroport("Toshkent Xalqaro Aeroporti", "Toshkent, O'zbekiston")
aviakompaniya1 = Aviakompaniya("Uzbekistan Airways", 1992)
aviakompaniya2 = Aviakompaniya("Turkish Airlines", 1933)

aeroport1.qoshish(aviakompaniya1)
aeroport1.qoshish(aviakompaniya2)
aeroport1.chiqar()

