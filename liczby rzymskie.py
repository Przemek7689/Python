print("Witaj w konwerterze liczb dziesiętnych na liczby rzymskie.")
print("Maksymalna liczba ma wartość 5000")

liczbyrzymskie={
    1:"I",
    5:"V",
    9:"IX",
    10:"X",
    40:"XL",
    50:"L",
    90:"XC",
    100:"C",
    400:"CD",
    500:"D",
    900:"CM",
    1000:"M"}
liczb_dziesietna=int(input("Podaj liczbe dziietną do 3999."))
while liczba_dziesietna<1 or liczba_dziesietna>=3999:    
    print("Podałeś złą liczbę")
    liczba_dziesietna=int(input("Podaj liczbe jeszcze raz"))

liczba_rzymska= ""
for key in sorted(liczbyrzymskie.keys(), reverse=True):
    

