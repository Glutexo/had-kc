from random import randrange

def nakresli_mapu(souradnice,ovoce):
    "Funkce dostane seznam souřadnic a vypíše je jako mapu"
    #Vytvoření tabulky
    tabulka = []
    for a in range(10):
        radek = []
        for b in range(10):
            radek.append(".")
        tabulka.append(radek)
    #Doplnění X (had) dle souřadnic
    for x,y in souradnice:
        (tabulka[y])[x]="X"
    #Doplnění ? (ovoce) dle souřadnic
    for m,n in ovoce:
        (tabulka[n])[m]="?"
    #Vypsání tabulky
    for radek in tabulka:
        for tecka in radek:
            print(tecka, end=' ')
        print()

def pohyb(souradnice,strana,ovoce):
    "Funkce přidá k seznamu poslední bod posunutý v daném směru"
    x=((souradnice[-1])[0])
    y=((souradnice[-1])[1])
    if strana=="v":
        souradnice.append((x,y+1))
    elif strana=="j":
        souradnice.append((x+1,y))
    elif strana=="s":
        souradnice.append((x,y-1))
    else:
        souradnice.append((x-1,y))
    #Vyhodnocení ovoce
    if souradnice[-1] in ovoce:                #Had vyroste a vytvoří se nové ovoce
        while True:
            ovoce=[(m,n)]
            if ovoce not in souradnice:
            m=randrange(0,10)
            n=randrange(0,10)
                break
    else:                                                   #Had se zkrátí
        del souradnice[0]

ovoce=[(2,3)]                                   #Počáteční ovoce a souřadnice.
souradnice=[(0,0),(1,0),(2,0)]
while True:
    strana=input("Na jakou stranu chceš hrát?(s,j,v,z):")
    pohyb(souradnice,strana,ovoce)
    nakresli_mapu(souradnice,ovoce)
