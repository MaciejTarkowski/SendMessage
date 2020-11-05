from datetime import datetime, timedelta
from szyfrator import Szyfrator
class Wiadomosc:
    wyslane_przez = ""
    wiadomosc = ""
    kod_wiadomosci = ""
    czas_wyslania = ""
    def __init__(self,wiadomosc_dic):
        szyfrator = Szyfrator()
        self.wyslane_przez = wiadomosc_dic["wyslane_przez"]
        self.wiadomosc = wiadomosc_dic["wiadomosc"]
        now = datetime.now()
        self.czas_wyslania = now.strftime("%Y%m%d%H%M%S")
        self.kod_wiadomosci = szyfrator.generujKod(self.czas_wyslania)
    
    def getWiadomosc(self):
        wiadomosc = {"wyslane_przez":self.wyslane_przez,"wiadomosc":self.wiadomosc,"czas_wyslania":self.czas_wyslania,"kod_wiadomosci":self.kod_wiadomosci}
        return wiadomosc
    
    def getIleMinelo(self,od_kiedy = czas_wyslania):
        od_kiedy = datetime.strptime(self.czas_wyslania,"%Y%m%d%H%M%S")
        print(od_kiedy)
        ile_minelo = datetime.now() - od_kiedy
        print(ile_minelo)
        return ile_minelo.total_seconds()
    
    def getGdzieDoleciala(self):
        c = 2.997 * 10**8 # predkosc fali
        wartosc = c * self.getIleMinelo()/1000
        human_readable_number = "{:,.0f}".format(wartosc)
        return human_readable_number # zwraca wartosc w kilometrach
    
    

    