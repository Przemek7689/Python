import random


print("Witaj w grze wisielca, podaj swoje imię: ")
imie = input()


lista = ["telefon", "ksiazka", "marker", "neandertalczyk", "zabawka","klocki","puzzle","wiatrak","sciana","ksiezyc","kot","samolot","deszcz","lampka","polaczenie","chusteczka","paleczka","nieskonczonosc"]

haslo = str(lista[random.randint(0, len(lista) - 1)])
tablica = list(haslo)
   
for i in range(len(haslo)):
    tablica[i] = "_"

zycie = 10

while zycie > 0:
    print("")
    print(imie, " pozostalo ci ", zycie, " zyc")
    print("")
    print(" ".join(tablica))
    print(" ")


    print("Podaj swoja litere: ")
    litera = input()

   
    if litera in haslo:
        for i in range(len(haslo)):
            if haslo[i] == litera:
                tablica[i] = litera
        if "".join(map(str, tablica)) == haslo:
            print("")
            print(imie, " pozostalo ci ", zycie, " zyc")
            print("")
            print(" ".join(tablica))
            print(" ")
            print("Gratulacje", imie, "wygrałaś!")
            break
    else:
        zycie -= 1
        print("Niestety tym razem się nie udało")
