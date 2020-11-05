class Menu():
    def wiadomosc_powitalna(self):
        print("Wyślij wiadomość w kosmos")

    def menu_glowne(self):
        print("Wybierz akcję wiadomosci")
        print("1. Wyślij nową wiadomość")
        print("2. Sprawdź swoją wiadomość")
        print("0. Wyjście")
        wybor =input("Wybór: ")
        return wybor
        
    def sprawdzanie_wiadomosci(self):
        kod_wiadomosci = input("Podaj kod swojej wiadomosci:\n")
        return kod_wiadomosci
        
    def menu_nowej_wiadomosci(self):
        print("Wybierz typ wiadomosci")
        print("1. Wiadomość tekstowa")
        print("2. Wiadomość obrazkowa")
        print("3. Wiadomość głosowa")
        print("0. Powrót")
        wybor =input("Wybór: ")
        return wybor


    def tworzenie_wiadomosci_tekstowej(self):
        wyslane_przez = input("Wpisz od kogo jest wiadomość:\n")
        wiadomosc = input("Wpisz swoją wiadomość:\n")
        nowa_wiadomosc = {"wyslane_przez": wyslane_przez,
                          "wiadomosc":wiadomosc}
        return nowa_wiadomosc
