#! /usr/bin/python
# -*- coding: utf-8 -*-

import sys
import traceback

# Sieb des Eratosthenes
def prim(MAX):
    # Create List:
    LIST = list(range(2, MAX))
    RES = []

    #Filtere Liste
    for num in LIST:
        if num in LIST and num != 1:
            if num >= MAX**0.5:
                break
            elif num in LIST:
                RES.append(num)
                LIST = filter(lambda x: x % num != 0, LIST)

    RES += LIST
    return RES

    
# Primfaktorzerlegung
def primfak(NUMBER):
    PRIMS = prim(NUMBER + 1)
    RES = []
    ERG = 0
    
    # Wenn übergebene Nummer eine Primzahl ist, ist die Primfaktorzerlegung bekannt
    if NUMBER in PRIMS:
        return {NUMBER: 1}
    
    while not ERG in PRIMS:
        for primn in PRIMS:            # Geht alle Primzahlen durch
            if NUMBER % primn == 0:    # Sobald eine Primzahl gefunden wurde, die NUMBER Teilt
                RES.append(primn)      # Füge diese Primzahl zu RES hinzu
                ERG = NUMBER / primn   # ERG enthält nun die übrigen Primzahlen
                if ERG in PRIMS:       # Sobald ERG eine Primzahl ist, wird ERG zu RESULT hinzugefügt
                    RES.append(ERG)
                NUMBER = ERG           # Erneuert NUMBER mit ERG
                break                  # Beendet die For-Schleife und fängt somit von vorne an
                
    ERG = {}

    for value in RES:
        if value in ERG:               # Fügt dem Dictionary ERG den Key Value hinzu
            ERG[value] += 1            # Erhöht den Exponenten von dem Key Value um einen
        else:
            ERG[value] = 1             # Fügt Value den Wert 1 zu

    return ERG


# Größter gemeinsamer Teiler nach Primfaktorzerlegung
def ggT_prim(NUM1, NUM2):
    PRIM_1 = primfak(NUM1)
    PRIM_2 = primfak(NUM2)
    RES    = []
    
    # Legt geordnete Liste mit den gleichen Werten von PRIM_1 und PRIM_2 an
    SAME = list(set(PRIM_1.keys()).intersection(PRIM_2.keys()))

    for VAL in SAME:
        if PRIM_1[VAL] >= PRIM_2[VAL]:
            RES += [VAL for _ in range(PRIM_2[VAL])]
        else:
            RES += [VAL for _ in range(PRIM_1[VAL])]

    if RES:
        return reduce(lambda x, y: x*y, RES)
    else:
        return "No ggT"



# Größter gemeinsamer Teiler nach euklidischem Algorithmus
def ggT(NUM1, NUM2):
    # Form: DIVIDENT = k * DIVISOR + REST
    # Es gilt NUM1 >= NUM2 und NUM1, NUM2 > 0
    
    if not NUM1 >= NUM2:
        NUM1 = NUM2
        NUM2 = NUM1
    if NUM1 <= 0 or NUM2 <= 0:
        raise ValueError
    
    DIVIDENT = NUM1
    DIVISOR = NUM2
    REST = 1
    
    while REST != 0:
        REST = DIVIDENT % DIVISOR
        DIVIDENT = DIVISOR
        DIVISOR = REST
    
    return DIVIDENT



# Kleinstes gemeinsames Vielfaches
def kgV(NUM1, NUM2):
    PRIM_1 = primfak(NUM1)
    PRIM_2 = primfak(NUM2)
    BOTH   = set(PRIM_1.keys() + PRIM_2.keys())
    RES    = []

    for VAL in BOTH:
        if VAL in PRIM_1 and VAL in PRIM_2:
            if PRIM_1[VAL] >= PRIM_2[VAL]:
                RES += [VAL for _ in range(PRIM_1[VAL])]
            else:
                RES += [VAL for _ in range(PRIM_2[VAL])]
        elif not VAL in PRIM_1:
            RES += [VAL for _ in range(PRIM_2[VAL])]
        else:
            RES += [VAL for _ in range(PRIM_1[VAL])]

    return reduce(lambda x, y: x*y, RES)


if __name__ == "__main__":
    try:
        FUNC = sys.argv[1]
    
        if len(sys.argv) > 2: NUM1 = int(sys.argv[2])
        if len(sys.argv) > 3: NUM2 = int(sys.argv[3])
        
        if FUNC in ["-p", "--prim"]:
            print "\n".join(map(lambda x: str(x), prim(NUM1)))
        elif FUNC in ["-pf", "--primfak"]:
            print primfak(NUM1)
        elif FUNC in ["--ggT-prim"]:
            print ggT_prim(NUM1, NUM2)
        elif FUNC in ["-g", "--ggT"]:
            print ggT(NUM1, NUM2)
        elif FUNC in ["-k", "--kgV"]:
            print kgV(NUM1, NUM2)
        elif FUNC in ["-h", "--help"]:
            print "-p  --prim    Berechnet alle Primzahlen bis zur Angegebenen Zahl"
            print "-pf --primfak Berechnet die Primfaktorzerlegung der Ang. Zahl"
            print "--ggT-prim    Berechnet den ggT zweier Zahlen mit Primzahlen (langsamer!)"
            print "-g --ggT      Berechnet den ggT zweier Zahlen"
            print "-k --kgV      Berechnet den kgV zweier Zahlen"
            print "-h --help     Zeigt diese Hilfe \n"
            
    except (IndexError, NameError, ValueError), e:
        sys.exit("Fehler bei der Eingabe %s" % e)
    
    except:
        sys.exit("Unerwarteter Fehler aufgetreten")
