import string
from datetime import datetime
class Szyfrator():
    szyfr = string.ascii_lowercase
    rozkodowana_data = ""
    def generujKod(self,data):
        kod = []
        for x in data:
            x = int(x) * 3
            kod.append(self.szyfr[x])
        return ''.join(kod)
    
    def rozkodujKod(self,kod):
        kod.lower()
        data = []
        for k in kod:
            data.append(str(int(self.szyfr.index(k)/3)))
        self.rozkodowana_data = ''.join(data)
        return datetime.strptime(self.rozkodowana_data,"%Y%m%d%H%M%S")
            
    def getIleMinelo(self):
        od_kiedy = datetime.strptime(self.rozkodowana_data,"%Y%m%d%H%M%S")
        ile_minelo = datetime.now() - od_kiedy
        return ile_minelo.total_seconds()
    
    def getGdzieDoleciala(self):
        c = 2.997 * 10**8 # predkosc fali
        wartosc = c * self.getIleMinelo()/1000
        human_readable_number = "{:,.0f}".format(wartosc)
        return human_readable_number # zwraca wartosc w kilometrach
            
