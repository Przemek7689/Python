print("Witaj w LOTTO")
print("Podaj 6 losowych liczb, pamietaj aby sie nie powtarzaly")
Lista2 = [3,4,5,6,7,10]
numer = 0
a=int(input("Podaj liczbe 1:  "))
b=int(input("Podaj liczbe 2:  "))
c=int(input("Podaj liczbe 3:  "))
d=int(input("Podaj liczbe 4:  "))
e=int(input("Podaj liczbe 5:  "))
f=int(input("Podaj liczbe 6:  "))
Lista=[a,b,c,d,e,f]
for g in range(0,5):
    for i in range(0,5):
            if Lista[g]==Lista2[i]:
                numer = numer + 1

print("Trafiłeś",  " ",numer)
