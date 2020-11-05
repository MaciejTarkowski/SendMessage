# Plik glowny
# Menu i wysylanie wiadomosci
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
        if menu_wiadomosci_wybor == "1":
            wiadomosc_dic = menu.tworzenie_wiadomosci_tekstowej()
            wiadomosc = Wiadomosc(wiadomosc_dic)
            print(wiadomosc.getWiadomosc())
    elif menu_glowne_wybor == "2":
        kod = menu.sprawdzanie_wiadomosci()
        szyfrator = Szyfrator()
        try:
            print(f'Twoja wiaodmość została wysłana {szyfrator.rozkodujKod(kod)}\n Pokonala dystans {szyfrator.getGdzieDoleciala()} km!')
        except:
            print("Twoj kod wygląda na niepoprawny, spróbuj ponownie")
        

