def pole_kwadratu(a):
    S = a * a
    return S
 
 
def pole_prostokata(a, b):
    S = a * b
    return S
 
 
def pole_trojkata(a, h):
    S = a * h / 2
    return S
 
 
def pole_rombu(e, f):
    S = e * f / 2
    return S
 
 
def pole_rownolegloboku(a, h):
    S = a * h
    return S
 
 
def pole_trapezu(a, b, h):
    S = (a + b) * h / 2
    return S
 
 
def pole_kola(r):
    S = 3.14 * r * r
    return S
 
 
poczatkowa_wiadomosc = """ Oto lista figur dla których można policzyć pole:
1 - kwadrat
2 - prostokąt
3 - trójkąt
4 - romb
5 - równoległobok
6 - trapez
7 - koło """
print(poczatkowa_wiadomosc)
figura = input("Wprowadź numer figury od 1 do 7: ")
print("Wybrana figura to: ", figura)
if figura == "1":
    a = input("Wprowadź długość boku kwadratu: ")
    a = float(a)
    S = pole_kwadratu(a)
    print("Pole kwadratu wynosi: ", S)
elif figura == "2":
    a = input("Wprowadź dłuższy bok prostokąta: ")
    a = float(a)
    b = input("Wprowadź krótszy bok prostokąta: ")
    b = float(b)
    S = pole_prostokata(a, b)
    print("Pole prostokąta wynosi:", S)
elif figura == "3":
    a = input("Wprowadź podstawę trójkąta: ")
    a = float(a)
    h = input("Wprowadź wysokość trójkąta: ")
    h = float(h)
    S = pole_trojkata(a, h)
    print("Pole trójkąta wynosi: ", S)
elif figura == "4":
    e = input("wprowadź krótszą przekątną rombu: ")
    e = float(e)
    f = input("Wprowadź dłuższą przekątną rombu: ")
    f = float(f)
    S = pole_rombu(e, f)
    print("Pole rombu wynosi: ", S)
elif figura == "5":
    a = input("wprowadź podstawę równoległoboku: ")
    a = float(a)
    h = input("wprowadź wysokość równoległoboka: ")
    h = float(h)
    S = pole_rownolegloboku(a,h)
    print("Pole równoległoboka wynosi: ", S)
elif figura == "6":
    a = input("Wprowadź krótszą podstawę trapezu: ")
    a = float(a)
    b = input("Wprowadź dłuższą podstawę trapezu: ")
    b = float(b)
    h = input("Wprowadź wysokość trapezu: ")
    h = float(h)
    S = pole_trapezu(a,b,h)
    print("Pole trapezu wynosi: ", S)
elif figura == "7":
    r = input("Wprowadź promień koła: ")
    r = float(r)
    S = pole_kola(r)
    print("Pole koła wynosi: ", S)
else:
    print("Nie ma figury pod numerem ", figura, ". Dostępne numery od 1 do 7.")