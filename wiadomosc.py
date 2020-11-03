from datetime import datetime, timedelta
class Wiadomosc:
    wyslane_przez = ""
    wiadomosc = ""
    kod_wiadomosci = ""
    czas_wyslania = datetime.now()
    def __init__(self,wiadomosc_dic):
        self.wyslane_przez = wiadomosc_dic["wyslane_przez"]
        self.wiadomosc = wiadomosc_dic["wiadomosc"]
    
    def getWiadomosc(self):
        wiadomosc = {"wyslane_przez":self.wyslane_przez,"wiadomosc":self.wiadomosc,"czas_wyslania":self.czas_wyslania}
        return wiadomosc
    
    def getIleMinelo(self):
        ile_minelo = datetime.now() - self.czas_wyslania
        return ile_minelo.total_seconds()
    
    def getGdzieDoleciala(self):
        c = 2.997 * 10**8 # predkosc fali
        wartosc = c * self.getIleMinelo()/1000
        human_readable_number = "{:,.0f}".format(wartosc)
        return human_readable_number # zwraca wartosc w kilometrach
    
    

    