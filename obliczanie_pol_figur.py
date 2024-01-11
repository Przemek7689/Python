def pole_kwadratu(a):
    P = a * a
    return P
def pole_prostokata(a, b):
    P = a * b
    return P
def pole_rownolegloboku(a, h):
    P = a * h
    return P
def pole_rombu(e, f):
    P = e * f
    return P
def pole_trojkata(a, h):
    P =(a * h)/2
    return P
def pole_trapezu(a, b, h):
    P = ((a + b)*h)/2
    return P
def pole_kola(r):
    P = 3,14*(r**2)
    return P

print("witaj w kalkulatorze pól figur.")
dla_uzytkownika = """ Oto lista figur dla których można policzyć pole:
1 - kwadrat
2 - prostokąt
3 - równoległobok
4 - romb
5 - trójkąt
6 - trapez
7 - koło """
print(dla_uzytkownika)
wybor = input("Wpisz numer figury od 1 do 7: ")
print("Wybrałeś figure numer: ", wybor)
if wybor == "1":
    a = input("Wpisz długość boku kwadratu: ")
    a = int(a)
    P = pole_kwadratu(a)
    print("Pole kwadratu wynosi: ", P)
elif wybor == "2":
    a = input("Wpisz długość dłuższego boku prostokąta: ")
    b = input("Wpisz długość krótszego boku prostokąta: ")
    a = int(a)
    b = int(b)
    P = pole_prostokata(a, b)
    print("Pole prostokąta wynosi:", P)
elif wybor == "3":
    a = input("wprowadź podstawę równoległoboku: ")
    h = input("wprowadź wysokość równoległoboka: ")
    a = int(a)
    h = int(h)
    P = pole_rownolegloboku(a,h)
    print("Pole równoległoboka wynosi: ", P)
elif wybor == "4":
    e = input("wprowadź krótszą przekątną rombu: ")
    f = input("Wprowadź dłuższą przekątną rombu: ")
    e = int(e)
    f = int(f)
    P = pole_rombu(e, f)
    print("Pole rombu wynosi: ", P)
elif wybor == "5":
    a = input("Wprowadź podstawę trójkąta: ")
    h = input("Wprowadź wysokość trójkąta: ")
    a = int(a)
    h = int(h)
    P = pole_trojkata(a, h)
    print("Pole trójkąta wynosi: ", P)
elif wybor == "6":
    a = input("Wprowadź krótszą podstawę trapezu: ")
    b = input("Wprowadź dłuższą podstawę trapezu: ")
    h = input("Wprowadź wysokość trapezu: ")
    a = int(a)
    b = int(b)
    h = int(h)
    P = pole_trapezu(a,b,h)
    print("Pole trapezu wynosi: ", P)
elif wybor == "7":
    r = input("Wprowadź promień koła: ")
    r = int(r)
    P = pole_kola(r)
    print("Pole koła wynosi: ", P)
else:
    print("Nie ma opcjii: ", wybor, ". Możesz wybrać tylko numery od 1 do 7.")