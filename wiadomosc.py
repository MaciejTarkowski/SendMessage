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
        self.kod_wiadomosci = szyfrator.generuj_kod(self.czas_wyslania)
    
    def get_wiadomosc(self):
        wiadomosc = {"wyslane_przez":self.wyslane_przez,"wiadomosc":self.wiadomosc,"czas_wyslania":self.czas_wyslania,"kod_wiadomosci":self.kod_wiadomosci}
        return wiadomosc
    
    def wyslij_wiadomosc(self):
        print("Wiadomość wysłana!",self.get_wiadomosc())
 
    
    

    