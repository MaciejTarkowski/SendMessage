import string
from datetime import datetime
class Szyfrator():
    szyfr = string.ascii_lowercase
    rozkodowana_data = ""
    def generuj_kod(self,data):
        kod = []
        for x in data:
            x = int(x) * 2
            kod.append(self.szyfr[x])
        return ''.join(kod)
    
    def rozkoduj_kod(self,kod):
        kod.lower()
        data = []
        for k in kod:
            data.append(str(int(self.szyfr.index(k)/2)))
        self.rozkodowana_data = ''.join(data)
        return datetime.strptime(self.rozkodowana_data,"%Y%m%d%H%M%S")
            
    def get_ile_minelo(self):
        od_kiedy = datetime.strptime(self.rozkodowana_data,"%Y%m%d%H%M%S")
        ile_minelo = datetime.now() - od_kiedy
        return ile_minelo.total_seconds()
    
    def get_gdzie_doleciala(self):
        c = 2.997 * 10**8 # predkosc fali
        wartosc = c * self.get_ile_minelo()/1000
        human_readable_number = "{:,.0f}".format(wartosc)
        return human_readable_number # zwraca wartosc w kilometrach
            
