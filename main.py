# Plik glowny
# Menu i wysylanie wiadomosci
# eaeaccasamcmkm - kod testowej wiadomosci
from menu import Menu
from wiadomosc import Wiadomosc
from szyfrator import Szyfrator

menu = Menu()

menu.wiadomosc_powitalna()
menu_glowne_wybor = "-1"

while menu_glowne_wybor != "0":
    menu_glowne_wybor = menu.menu_glowne()
    if menu_glowne_wybor == "1":
        menu_wiadomosci_wybor = menu.menu_nowej_wiadomosci()
        wiadomosc_dic = menu.tworzenie_wiadomosci(menu_wiadomosci_wybor)
        if wiadomosc_dic != 0:
            wiadomosc = Wiadomosc(wiadomosc_dic)
            wiadomosc.wyslij_wiadomosc()
    elif menu_glowne_wybor == "2":
        kod = menu.sprawdzanie_wiadomosci()
        szyfrator = Szyfrator()
        try:
            print(f'Twoja wiaodmość została wysłana {szyfrator.rozkoduj_kod(kod)}\n Pokonala dystans {szyfrator.get_gdzie_doleciala()} km!')
        except:
            print("Twoj kod wygląda na niepoprawny, spróbuj ponownie")