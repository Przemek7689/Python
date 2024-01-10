print("Witaj w konwerterze liczb dziesiętnych na liczby rzymskie.")

from collections import OrderedDict
def pisz_system_rzymski(liczba):

   liczbyrzymskie = OrderedDict()
   liczbyrzymskie[1000] = "M"
   liczbyrzymskie[900] = "CM"
   liczbyrzymskie[500] = "D"
   liczbyrzymskie[400] = "CD"
   liczbyrzymskie[100] = "C"
   liczbyrzymskie[90] = "XC"
   liczbyrzymskie[50] = "L"
   liczbyrzymskie[40] = "XL"
   liczbyrzymskie[10] = "X"
   liczbyrzymskie[9] = "IX"
   liczbyrzymskie[5] = "V"
   liczbyrzymskie[4] = "IV"
   liczbyrzymskie[1] = "I"


   def system_rzymski_liczba(liczba):
        for i in liczbyrzymskie.keys():
            a, b = divmod(liczba, i)
            yield liczbyrzymskie[i] * a
            liczba -= (i * a)
            if liczba > 0:
                system_rzymski_liczba(liczba)
            else:
                break

   return "".join([a for a in system_rzymski_liczba(liczba)])
liczba = int(input("Podaj liczbę dziesiętną, którą chcesz przekonwertować na liczbę rzymską: "))
print ("Liczba" ,liczba , "w systemie rzymskim to: ",pisz_system_rzymski(liczba))

