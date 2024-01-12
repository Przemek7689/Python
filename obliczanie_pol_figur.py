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

print("                               ")
print("Witaj w kalkulatorze pól figur.")
print("                               ")
dla_uzytkownika = """Oto lista figur dla których możesz obliczyć pole:
1 - kwadrat
2 - prostokąt
3 - równoległobok
4 - romb
5 - trójkąt
6 - trapez
7 - koło """
print(dla_uzytkownika)
print("                               ")
wybor = input("Wpisz numer figury, której pole chcesz obliczyć (od 1 do 7): ")
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
    a = input("Wpisz długość boku równoległoboku: ")
    h = input("Wpisz długość wysokości równoległoboku: ")
    a = int(a)
    h = int(h)
    P = pole_rownolegloboku(a,h)
    print("Pole równoległoboku wynosi: ", P)
elif wybor == "4":
    e = input("Wpisz długość dłuższej przekątnej rombu: ")
    f = input("Wpisz długość krótszej przekątnej rombu: ")
    e = int(e)
    f = int(f)
    P = pole_rombu(e, f)
    print("Pole rombu wynosi: ", P)
elif wybor == "5":
    a = input("Wpisz długość podstawy trójkąta: ")
    h = input("Wpisz długość wysokości trójkąta: ")
    a = int(a)
    h = int(h)
    P = pole_trojkata(a, h)
    print("Pole trójkąta wynosi: ", P)
elif wybor == "6":
    a = input("Wpisz długość krótszej podstawy trapezu: ")
    b = input("Wpisz długość dłuższej podstawy trapezu: ")
    h = input("Wpisz długość wysokości trapezu: ")
    a = int(a)
    b = int(b)
    h = int(h)
    P = pole_trapezu(a,b,h)
    print("Pole trapezu wynosi: ", P)
elif wybor == "7":
    r = input("Wpisz długość promienia koła: ")
    r = int(r)
    P = pole_kola(r)
    print("Pole koła wynosi: ", P)
else:
    print("Nie ma opcjii: ", wybor, ". Możesz wybrać tylko numery od 1 do 7.")