import math
import random
import nuovoModulo as nm
import altroModulo as am
import datetime

print("-----------------------ESERCIZIO 1------------------------")
'''
Esercizio 1
Importa il modulo math e calcola la radice quadrata di 16.
'''
x1 = 16 
print (math.sqrt(x1))

print("-----------------------ESERCIZIO 2------------------------")
'''
Esercizio 2
Importa il modulo random e genera un numero casuale compreso tra 1 e 10..
'''
x2 = random.randrange(1,10)
print(x2)

print("-----------------------ESERCIZIO 3------------------------")
'''
Esercizio 3
Crea un nuovo file Python chiamato nuovo_modulo.py e definisci una funzione chiamata somma che prende due argomenti e restituisce la loro somma. Poi importa il modulo nel tuo programma principale e usa la funzione somma.
'''
x3 = nm.somma(x1, x2)
print("somma di 25 e rand 2:",x3)

print("-----------------------ESERCIZIO 4------------------------")
'''
Esercizio 4
Crea un nuovo file Python chiamato altro_modulo.py e definisci una variabile chiamata lista_numeri che contiene una lista di numeri interi. Poi importa il modulo nel tuo programma principale e stampa la lista. Prova con un ciclo for a stampare ogni elemento della lista.
'''
for x4 in am.listaNumeri:
    print(x4)

print("-----------------------ESERCIZIO 5------------------------")
'''
Esercizio 5
Scrivi un programma che stampa la data e l'ora corrente.
'''
x5 = datetime.datetime.now()
print(x5)

print("-----------------------ESERCIZIO 6------------------------")
'''
Esercizio 6
Scrivi un programma che prende in input una data in formato "gg/mm/aaaa" e stampa il nome del mese corrispondente.
'''
iDataGGMMAAAA = input("Inserisci una data in formato gg/mm/aaaa: ")
iDataGGMMAAAA = "11/11/1111"
# Conversione della stringa in oggetto datetime
iData = datetime.datetime.strptime(iDataGGMMAAAA, "%d/%m/%Y")
mesi = {
    1: "Gennaio", 2: "Febbraio", 3: "Marzo", 
    4: "Aprile", 5: "Maggio", 6: "Giugno",
    7: "Luglio", 8: "Agosto", 9: "Settembre", 
    10: "Ottobre", 11: "Novembre", 12: "Dicembre"
}
print(f"Il mese corrispondente è: {mesi[iData.month]}")

print("-----------------------ESERCIZIO 7------------------------")
'''
Esercizio 7
Scrivi un programma che prende in input due date e calcola la differenza in giorni tra le due.
'''
x7 = input("Inserisci una data in formato gg/mm/aaaa: ")
x7 = "11/11/1112"
iData2 = datetime.datetime.strptime(x7, "%d/%m/%Y")
if iData2 < iData:
    iData, iData2 = iData2, iData
differenza = abs((iData2 - iData).days)
print(f"La differenza in giorni tra le due date è: {differenza}")

print("-----------------------ESERCIZIO 8------------------------")
'''
Esercizio 8
Importa il modulo math e utilizza la funzione utile a calcolare la potenza di 2 elevato alla 3
'''
x8 = math.pow(2, 3)
print ("Potenza di 2^3",x8)

print("-----------------------ESERCIZIO 9------------------------")
'''
Esercizio 9
Importa il modulo math e utilizza la funzione utile a calcolare la radice quadrata di 25.
'''
x9 = 25 
print (math.sqrt(x9))

print("-----------------------ESERCIZIO 10------------------------")
'''
Esercizio 10
Importa il modulo math e utilizza la funzione utile a arrotondare un numero float a un intero inferiore.
'''
x10 = math.floor(2.55)
print(x10)

print("-----------------------ESERCIZIO 11------------------------")
'''
Esercizio 11
Importa il modulo math e utilizza la funzione utile ad arrotondare un numero float a un intero superiore
'''
x11 = math.ceil(2.55)
print(x11)

print("-----------------------ESERCIZIO 12------------------------")
'''
Esercizio 12
Importa il modulo math e utilizza la funzione adeguata per calcolare il fattoriale del numero 12.
'''
x11 = math.factorial(5)
print(x11)

print("-----------------------ESERCIZIO 13------------------------")
'''
Esercizio 13
Scrivere una funzione “giorno_settimana” che prenda in input una data come oggetto datetime e restituisca in output il giorno della settimana corrispondente in formato stringa in italiano.
'''
iData3GGMMAAAA = input("Inserisci una data in formato gg/mm/aaaa: ")
iData3GGMMAAAA = "11/11/1113"
iData3 = datetime.datetime.strptime(iData3GGMMAAAA, "%d/%m/%Y")

def giornoSettimana(iData3):
    giorni = {
        0: "Lunedì", 1: "Martedì", 2: "Mercoledì",
        3: "Giovedì", 4: "Venerdì", 5: "Sabato", 6: "Domenica"
    }
    print(giorni[iData3.weekday()])

giornoSettimana(iData3)

print("-----------------------ESERCIZIO 14------------------------")
'''
Esercizio 14
Scrivere un programma Python per selezionare un elemento casuale da una lista, un insieme e un un dizionario.
'''
list14 = [1, 2, 3, 4, 5]
set14 = {6, 7, 8, 9, 10}
dict14 = {11: "a", 12: "b", 13: "c", 14: "d", 15: "e"}

x14 = list14 + list(set14) + list(dict14.keys())
randX14 = random.choice(x14)
 # randX14 = 15
if randX14 in dict14:
    print(f"Elemento casuale: {randX14}, nel dizionario con valore: {dict14[randX14]}")
else:
    print(f"Elemento casuale: {randX14}")

print("-----------------------ESERCIZIO 15------------------------")
'''
Esercizio 15
Scrivere un programma Python per generare un numero intero casuale tra 0 e 6 - escluso 6, un numero intero casuale tra 5 e 10 - escluso 10, un numero intero casuale tra 0 e 10,
 con un intervallo di 3 e una data casuale tra due date.
'''
x15 = random.randint(0, 5) 
print(x15)
x15 = random.randint(5, 10)
print(x15)
x15 = random.choice(range(0, 10, 3))
print(x15)
iDataIntX15, iDataIntY16 = iData.toordinal(), iData2.toordinal()
randX15 = datetime.date.fromordinal(random.randint(iDataIntX15, iDataIntY16))
print(randX15)

print("-----------------------ESERCIZIO 16------------------------")
'''
Esercizio 16
Scrivere un programma Python per riordinare casualmente gli elementi di una lista.
'''


print("-----------------------ESERCIZIO 17------------------------")
'''
Esercizio 17
Scrivete un programma Python per generare un float compreso tra 0 e 1, incluso, e generare un float casuale all'interno di un intervallo specifico.
'''


print("-----------------------ESERCIZIO 18------------------------")
'''
Esercizio 18
Scrivere un programma Python per creare una lista di numeri interi casuali e selezionare casualmente più elementi da tale lista.
'''


print("-----------------------ESERCIZIO 19------------------------")
'''
Esercizio 19
Scrivere un programma per visualizzare i seguenti formati di data e ora:
a) Data e ora correnti
b) Anno corrente
c) Mese dell'anno
d) Numero della settimana dell'anno
e) Giorno della settimana
f) Giorno dell'anno
g) Giorno del mese
h) Giorno della settimana
'''
