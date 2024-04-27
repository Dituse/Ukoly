#Úkol 1: https://github.com/andywaltlova/programovani-v-pythonu-jaro-2024/blob/main/ukoly/ukol-1-zadani.md
#Autor: Dita Hronová

class Zvire:
    def __init__(self, jmeno: str, druh: str, vaha: int):
        self.jmeno = jmeno 
        self.druh = druh
        self.vaha = vaha
        
    def __str__(self):
        return f'{self.druh} se jmenuje {self.jmeno} a váží {self.vaha} kg.'

    def export_to_dict(self):
        return {'jmeno':self.jmeno, 'druh': self.druh, 'vaha':self.vaha}
    
    def vaha_vsech_zvirat_v_zoo(zvirata):
        total_weight = sum(animals['vaha'] for animals in zvirata)
        return total_weight


class Employee:
    def __init__(self, cele_jmeno:str, rocni_plat:int, pozice:str):
     self.cele_jmeno = cele_jmeno
     self.rocni_plat = rocni_plat
     self.pozice = pozice

    def __str__(self):
        return f'{self.cele_jmeno} pracuje na pozici {self.pozice} a vydělává {self.rocni_plat} Kč ročně.'
     
    def ziskej_inicialy(self):
        name = self.cele_jmeno.split( )
        return (name[0][0] + '. ' + name[1][0] + '.')

    def mesicni_naklady_na_zamestnance(zamestnanci, reditel):
        vyplata_zamestnanci = sum(employee['rocni_plat']/12 for employee in zamestnanci)
        vyplata_reditel = reditel.rocni_plat/12
        return vyplata_zamestnanci + vyplata_reditel


class Reditel(Employee):
    def __init__(self, cele_jmeno, rocni_plat, oblibene_zvire:Zvire, pozice='Ředitel'):
        super().__init__(cele_jmeno, rocni_plat, pozice)
        self.oblibene_zvire = oblibene_zvire


class Zoo:
    def __init__(self, jmeno:str, adresa:str, reditel:Reditel, zamestnanci:list[Employee],zvirata:list[Zvire]):
        self.jmeno = jmeno
        self.adresa = adresa
        self.reditel = reditel
        self.zamestnanci = zamestnanci
        self.zvirata = zvirata 


#jezek = Zvire("Růženka", "Ježek", 0.5)
#jezek_export = jezek.export_to_dict()

#print(jezek)
#print(jezek_export)

#assert jezek_export['jmeno'] == 'Růženka'
#assert jezek_export['druh'] == 'Ježek'
#assert jezek_export['vaha'] == 0.5

zvirata_dict = [
    {'jmeno': 'Helenka', 'druh': 'Panda Velká', 'vaha': 150},
    {'jmeno': 'Vilda', 'druh': 'Vydra Mořská', 'vaha': 20},
    {'jmeno': 'Matýsek', 'druh': 'Tygr Sumaterský', 'vaha': 300},
    {'jmeno': 'Karlík', 'druh': 'Lední medvěd', 'vaha': 700},
]

zvirata_obj = []
for animal in zvirata_dict:
    zvirata_obj.append(Zvire(animal['jmeno'], animal['druh'], animal['vaha']))


total_weight = Zvire.vaha_vsech_zvirat_v_zoo(zvirata_dict)
print(f'Váha všech zvířat v zoo je {total_weight} kg.')


#standa = Employee('Stanislav Novák', 520_000, 'Ošetřovatel zvířat')

#print(standa)
#print(standa.ziskej_inicialy())

zamestnanci_dict = [
    {'cele_jmeno': 'Tereza Vysoka', 'rocni_plat': 700_000, 'pozice': 'Cvičitelka tygrů'},
    {'cele_jmeno': 'Anet Krasna', 'rocni_plat': 600_000, 'pozice': 'Cvičitelka vyder'},
    {'cele_jmeno': 'Martin Veliky', 'rocni_plat': 650_000, 'pozice': 'Cvičitel ledních medvědů'},
]


zamestnanci_obj = []
for zamestnanec in zamestnanci_dict:
    zamestnanci_obj.append(list([zamestnanec['cele_jmeno'], zamestnanec['rocni_plat'], zamestnanec['pozice']]))


zvire = Zvire('Pepa', 'pavouk', 0.1)
reditel = Reditel(cele_jmeno='Karel', rocni_plat=800_000, oblibene_zvire=zvire)

assert reditel.pozice == 'Ředitel'
assert isinstance(reditel.oblibene_zvire, Zvire)

vyplata_zamestnanci = Employee.mesicni_naklady_na_zamestnance(zamestnanci_dict, reditel)
vyplata_zamestnanci=round(vyplata_zamestnanci)
print(f'Měsíční náklady na zaměstance jsou {vyplata_zamestnanci} Kč.')

# Zvire class
zvire = Zvire('Láďa', 'Koala', 15)
assert hasattr(zvire, 'jmeno')
assert hasattr(zvire, 'druh')
assert hasattr(zvire, 'vaha')
assert isinstance(zvire.jmeno, str)
assert isinstance(zvire.druh, str)
assert isinstance(zvire.vaha, int)
assert zvire.export_to_dict() == {'jmeno': 'Láďa', 'druh': 'Koala', 'vaha': 15}

# Zamestnanec class
zamestnanec = Employee('Petr Novak', 50000, 'Programator')
assert hasattr(zamestnanec, 'cele_jmeno')
assert hasattr(zamestnanec, 'rocni_plat')
assert hasattr(zamestnanec, 'pozice')
assert isinstance(zamestnanec.cele_jmeno, str)
assert isinstance(zamestnanec.rocni_plat, int)
assert isinstance(zamestnanec.pozice, str)
assert zamestnanec.ziskej_inicialy() == 'P. N.'

# Reditel class
zvire = Zvire('Lev', 'Lvice', 150)
reditel = Reditel('Jan Novotny', 80000, zvire)
assert isinstance(reditel.oblibene_zvire, Zvire)

# Zoo class
zoo = Zoo('Zoo Praha', 'Praha', reditel, [zamestnanec], [zvire])
assert hasattr(zoo, 'jmeno')
assert hasattr(zoo, 'adresa')
assert hasattr(zoo, 'reditel')
assert hasattr(zoo, 'zamestnanci')
assert hasattr(zoo, 'zvirata')
assert isinstance(zoo.jmeno, str)
assert isinstance(zoo.adresa, str)
assert isinstance(zoo.reditel, Reditel)
assert isinstance(zoo.zamestnanci, list)
assert isinstance(zoo.zvirata, list)
