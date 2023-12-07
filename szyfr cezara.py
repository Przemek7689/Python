def szyfr(napis, klucz):
    szyfry = ""
    for i in napis:
        litera = klucz + ord(i)
        if litera> ord('z'):
            litera -=26
        elif litera< ord('a'):
            litera +=26

    szyfry +=chr(litera)

    return szyfry

napis=''
klucz=3

szyfry= szyfr(napis, klucz)
print(szyfry)

szyfry= szyfr(szyfry, -klucz)
print(napis)