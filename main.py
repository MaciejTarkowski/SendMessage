# Plik glowny
# Menu i wysylanie wiadomosci
from menu import Menu
from wiadomosc import Wiadomosc

menu = Menu()

menu.wiadomosc_powitalna()
menu_glowne_wybor = menu.menu_glowne()
if menu_glowne_wybor == "1":
    menu_wiadomosci_wybor = menu.menu_nowej_wiadomosci()
    if menu_wiadomosci_wybor == "1":
        wiadomosc_dic = menu.menu_wiadomosci_tekstowej()
        wiadomosc = Wiadomosc(wiadomosc_dic)
        print(wiadomosc.getGdzieDoleciala(),'km')