def szyfruj(napis, klucz): 

    szyfrogram = "" 
    for i in napis: 
        litera = klucz + ord(i) 
        if litera > ord('z'): 
            litera -= 26
        elif litera < ord('a'):  
            litera += 26

        szyfrogram += chr(litera) 

    return szyfrogram


napis = 'abcxyz'
klucz = 2

szyfrogram = szyfruj(napis, klucz) 
print(szyfrogram)

napis = szyfruj(szyfrogram, -klucz)
print(napis) 




