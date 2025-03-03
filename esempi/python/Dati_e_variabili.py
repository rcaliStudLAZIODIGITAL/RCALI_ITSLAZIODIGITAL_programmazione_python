# QUESTO è UN COMMENTO

""" QUESTO è UN
COMMENTO MULTIRIGA"""

# SINTASSI PER DICHIARARE VARIABILI
x= 5
y= 10

# NOMENCLATURA CORRETTA:

# si possono dichiarare variabili in minuscolo:

pesospecifico= 65

#si può utilizzare lo snake_case
peso_specifico= 65

#si può utilizzare il CamelCase:

pesoSpecifico= 65

#si può utilizzare il PascalCase

PesoSpecifico= 65

#posso utilizzare anche dei numeri per il nome delle veriabili:
x1= 50
pesospecifico1 = 90
peso1specifico= 20

#LE COSTANTI SI DICHIARANO IN MAIUSCOLO
PESOSPECIFICO = 65 # attrenzione, python è case sensitive

# NOMENCLATURA ERRATA:

# non si utilizzano mai: trattini, spazi o nomi di variabili che cominciano con numeri
"""
2pesospecifico= 70
peso-specifico= 80
peso specifico= 40"""


# si possono dichiarare ed inizializzare le variabili in una sola riga:

# se vogliamo assegnare valori diversi alle variabili:
x,y,z = 30, 70, 35

# se vogliamo assegnare lo stesso valore alle variabili:

k = j = f = 20

# COME POSSIAMO UTILIZZARE LE VARIABILI?

# 1) si possono stampare nel terminale con la funzione print ---> print(nome_variabile)
print(k)
print("x=", x)

# 2) si possono utilizzare per fare delle operazioni:

somma = k+x

print("k+x=", somma )

# ----------- TIPI DI DATO ----------

# se vogliamo sapere che tipo di dato ha una variabile

d = 100
tipo_dato= type(d)

print(tipo_dato)
print("la variabile d è: ", type(d) )

#quali tipi di dato abbiamo?


# STRINGHE --> STR --> testo --> tra apici singoli o doppi

s= "ciao"
s1= "3"

# INTEGER --> INT --> numeri interi positivi o negativi:

i= 25
i1 = -30

# DECIMALI --> FLOAT --> numeri decimali positivi o negativi
f= 5.5
f1= -10.5 # attenzione al divisore decimale, deve essere un . !!

# BOOLEANI --> BOOL --> accetta solo valori True o False
# Attenzione: True e False devono avere sempre la prima lettera maiuscola!!!
b= True
b1= False

# LISTE ---> LIST --> collezione di dati ( simile ad Array)

citta= ['Roma', "Torino", "Napoli"]

numeri= [2,5,7]

elementi= ["ciao", -23, True]

# INPUT E OUTPUT:

# INPUT --> serve a ricevere dei tadi in input dal terminale 
# Attenzione: gestisce solo type String!!

#nome= input("inserisci il tuo nome ")
# la variabile nome avrà in memoria il nome inserito da terminale

# OUTPUT ---> serve a stampare a video
#print("ciao " , nome)

# CASTING --> serve a convertire i tipi di dato

a = "5"
b= 5

# per fare questa operazione possiamo fare il casting --> convertire il valore di a in un intero:
# print(int(a)+b)

# numero1= input("dammi un numero ")
# numero2= input("dammi un altro numero ")

# tot= int(numero1)+ int(numero2)

# print(tot)

# si può fare il casting con diversi datatype:

# DA INTERO A STRINGA
intero= 5
stringa= str(intero)

print(type(stringa))

# Da integer a Float

num1= 10
num2= float(num1)

print("num2 è : ", type(num2))
print(num2)







