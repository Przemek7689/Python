import random

print("Witaj w grze papier kamien nozyce")
print("1 - kamień")
print("2 - papier")
print("3 - nozyce")
wybor = int(input("Wybierz 1,2 lub 3"))
los=random.randit(1,3)

if wybor == 1 and los==1:
    print("Wybrałeś kamień")
    print("Komputer tez wybrał kamień")
    print("A więc mamy remis")
elif wybor == 1 and los==2:
    print("Wybrałeś kamień")
    print("Natomiast komputer wybrał papier")
    print("W rezultacie komputer wygrał")
elif wybor == 1 and los==3:
    print("Wybrałeś kamień")
    print("Natomiast komputer wybrał nozyce")
    print("Gratulacje Wygrałeś!!")
elif wybor == 2 and los==1:
    print("Wybrałeś papier")
    print("Natomiast komputer wybrał kamień")
    print("Gratulacje Wygrałeś!!")
elif wybor == 2 and los==2:
    print("Wybrałeś papier")
    print("Komputer tez wybrał papier")
    print("A więc mamy remis")
elif wybor == 2 and los==3:
    print("Wybrałeś papier")
    print("Natomiast komputer wybrał nozyce")
    print("W rezultacie komputer wygrał")
elif wybor == 3 and los==1:
    print("Wybrałeś nozyce")
    print("Natomiast komputer wybrał kamień")
    print("W rezultacie komputer wygrał")
elif wybor == 3 and los==2:
    print("Wybrałeś nozyce")
    print("Natomiast komputer wybrał papier")
    print("Gratulacje Wygrałeś!!")
elif wybor == 3 and los==3:
    print("Wybrałeś nozyce")
    print("Komputer tez wybrał nozyce")
    print("A więc mamy remis")
    



    

    