'''

'''
print("-----------------------ESERCIZIO 1------------------------")
def getListSum():
    numeri = [1,2,3,4,5]
    somma = 0
    for i in numeri:
        somma += i
    print("Somma valori elementi:",somma)

getListSum()

'''

'''
print("-----------------------ESERCIZIO 2------------------------")
def getListInv():
    numeri = [1,2,3,4,5]
    invNumeri = numeri[::-1]
    print("Valori invertiti:",invNumeri)

getListInv()

'''

'''
print("-----------------------ESERCIZIO 3------------------------")
def getParoleG():
    parole = ["albero", "cane", "gatto", "acqua"]
    paroleG = []
    for i in parole:
        if i.startswith("g"):
            paroleG.append(i)
        
    print("Parole che iniziano con la g:",paroleG)

getParoleG()

'''

'''
print("-----------------------ESERCIZIO 4------------------------")
def getNumP():
    numeri = [1,2,3,4,5]
    numeriP =[]
    for i in numeri:
        if i%2==0:
            numeriP.append(i)
    print("Lista dei valori pari nella lista numeri:",numeriP)

getNumP()

'''

'''
print("-----------------------ESERCIZIO 5------------------------")
def getLenS():
    s = "Ciao!"
    nChar = 0
    for i in s:
        nChar+=1
    print("Numero dei caratteri nella stringa",nChar)

getLenS()

'''

'''
print("-----------------------ESERCIZIO 6------------------------")
def getMaxN():
    numeri = [1,2,3,9,4,5]
    maxN = max(numeri)
    print(maxN)

getMaxN()

print("-----------------------ESERCIZIO 7------------------------")
def getMaxP():
    maxP = ""
    parole = ["albero", "cane", "gatto", "acqua"]
    for i in parole:
        if len(i) > len(maxP):
            maxP = i
    print(maxP)

getMaxP()

'''

'''
print("-----------------------ESERCIZIO 8------------------------")
def getListAvg():
    numeri = [1,2,3,4,5]
    valAvg = sum(numeri)/len(numeri)
    print("Valore media elementi:",valAvg)

getListAvg()

'''
Esercizio 9
Scrivi una funzione che, data una stringa come parametro, restituisca un dictionary rappresentante la "frequenza di comparsa" di ciascun carattere componente la stringa.
Per fare un esempio, data una stringa "ababcc", otterremo in risultato {"a": 2, "b": 2, "c": 2}
'''
print("-----------------------ESERCIZIO 9------------------------")
s = "Ciao!"
def getDictFreq(s):
    dict = {}
    for i in s:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    print(dict)

getDictFreq(s)

print("-----------------------ESERCIZIO 10-----------------------")
'''
Esercizio 10
Scrivi una funzione che, dato in ingresso un valore espresso in metri, memorizzi in un Dictionary l'equivalente in miglia terrestri, iarde, piedi e pollici. Mandare in stampa il dict.
'''
def getDictMisure(valM):
    if valM <= 0:
        valM = 1.0
        print("Valore non valido!, uso 1.0...")
        return
    dict = {
        "inch": round(valM * 39.37008, 3),   
        "feet": round(valM * 3.28084, 3),
        "yard": round(valM * 1.093613, 3),
        "mile": round(valM * 0.0006213712, 3)
        }
    print(dict)

getDictMisure(valM=float(input("Inserisci un valore in metri=")))