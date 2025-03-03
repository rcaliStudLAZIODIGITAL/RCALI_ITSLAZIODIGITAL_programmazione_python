# I MODULI --> un modulo è un file contenente codice riutiulizzabile (funzioni, variabili)
# possono essere considerati delle librerie

# IMPORTAZIONE DEL MODULO PERSONALIZZATO:

import MioModulo

MioModulo.saluta("Ciccio")

nome_persona1= MioModulo.persona1["nome"]

print(nome_persona1)

# SI POSSONO DARE ALIAS AL MODULO --> riassegnare un nome al modulo per facilità di scrittura

import MioModulo as Mm

Mm.saluta("Mario")
eta_persona1= Mm.persona1["eta"]
print(eta_persona1)

# POSSO IMPORTARE SOLO LA FUNZIONE:

from MioModulo import saluta
saluta("marta")

#posso importare anche più di una funz/variabile:
from MioModulo import saluta, persona1


# se in questo file dichiaro una funzione uguale a quella del modulo, in esecuzione questa avrà la priorità:
def saluta(nome):
    print("ciao")

saluta("x")

#---------------#

# moduli BUILT_IN:

# Modulo Platform --> metodi per avere info sulla piattaforma che sto utilizzando:

import platform
x= platform.system() # info sul SO
print(x)

# Modulo math --> funzioni per calcoli matematici
import math

arr_dif = math.floor(5.75) #---> arrotonda per difetto il numero passato come argomento
print(arr_dif)

arr_ecc = math.ceil(5.75) # ---> arrotonda per eccesso il numero passato come argomento
print(arr_ecc)

numeri= [1,2,3,4]

prodotto= math.prod(numeri) # --> restituisce il prodotto dei numeri in una collection
print(prodotto)

# modulo random --> ha funzioni per generare numeri casuali

import random

# random.randrange(x,y) --> genera un numero intero casuale compreso nel range definito come argomento:
num_range= random.randrange(3,15)
print("num random",num_range)

#random.uniform(x,y)--> genera un numero decimale casuale compreso nel range definito come argomento:

float_random= random.uniform(3,15)
print("float random",float_random)

#random.choice(collection) --> seleziona un elemento casuale dalla collection 

valore_cas= random.choice(numeri)
print("elemento random",valore_cas)

# questa funzione può essere utilizzata anche con tipo di dato diverso dai numeri:

lista= ["ciao", True, 25, "x"]
casuale= random.choice(lista)
print("elemento random 2:",casuale)

#anche con stringhe:
stringa= "buongiorno"
lett_random= random.choice(stringa)
print(lett_random)

#random.shuffle(sequence) --> riordina in modo casuale gli elementi
citta=["Roma", "Milano", "Bari"]
print(citta)

random.shuffle(citta)
print("shuffle:",citta)

# ----------------------------------#

#funzione dir(nome_modulo) ---> elenca le funzioni di un modulo passaro come argomento:

print(dir(random)) # ---> tutte le funzioni di random

# ----------------------------------#

# i PACKAGES : sono funzionalità extra ( non compresi nella lib. base) sviluppate da latre persone:

# pip --> package manager (installa / elimina pacchetti) 
# controllare se abbiamo già pip--> (nel terminale) pip --version
# se non lo abbiamo --> (nel terminale) get-pip.py --oppure-- python install pip
# documentazione per i packages --> www.pypi.org

# utilizzo di un package:

# esempio: voglio installare il package camelcase: 

# 1) nel terminale --> pip install camelcase (per installare il pacchetto)

# 2) import del modulo camelcase:
import camelcase

c= camelcase.CamelCase() # creo un oggetto per poter accedere al metodo hump()

# hump(str) --> prende una stringa come parametro e la trasforma in camelCase

frase= "questa è la frase da trasformare"
print(c.hump(frase))

#eliminare un pacchetto:
# nel terminale --> pip uninstall camelcase

#per sapere quali packages abbiamo:
# nel terminale --> pip list





