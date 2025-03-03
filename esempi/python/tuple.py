
# TUPLE 
# sono: ordirnate, indicizzate, NON modificabili, ammettono duplicati
# anche le tuple accettano valori di tipo di dato misto
# le riconosciamo dalle parentesi ()

#DICHIARAZIONE
x=("milano", "roma", "venezia")
print(x)

# possiamo dichiarare le tuple con il megtodi costruttore:
num= tuple((1,2,3,4))
print(num)

# METODI PER AVERE INFORMAZIONI SULLE TUPLE:

# TYPE() --> per sapere il tipo di dato ( <class tuple>)
print(type(x))

# LEN() --> di sapere la lunghezza della tupla
print(len(x))

# ACCEDERE AGLI ELEMENTI DELLE TUPLE:
# come per le liiste possiamo usare l'indice numerico:

print(x[0]) # primo elemento
print(x[-1]) # ultimo elemento
print(x[1:3]) # da 1 a 2 ( 3 escluso)

# per verificare se un valore è presente in una tupla:

if "ciao" in x :
    print("valore presente")
else:
    print("valore assente")

# possiamo fare UNPACK della tupla per creare delle variabili ( una per ogni elemento della tupla)

(citt1, citt2, citt3)= x
print("varibile 1:", citt1)
print("varibile 2:", citt2)
print("varibile 3:", citt3)

# ciclare gli elementi delle tuple:
for citta in x :
    print(citta)

# voglio stampare anche l'indice:

i= 0
for citta in x:
    print("elemento: ",i, citta )
    i+=1

# SI POSSONO UNIRE le TUPLE:
y= (1,2,3)
z= (4,2,2)

numeri= y+z
print(numeri)
print(type(numeri))

#METODO COUNT() --> conta quante voplte un valore è presente nella tupla
# si può utilizzare anche nelle liste

conteggio= numeri.count(2)
print("il valore è ripetuto" , conteggio, " volte")

# metodo index() --> restituisce l'indice di un elemento:
# si può utilizzare anche nelle liste

indice= x.index("roma")
print(indice)

#per eliminare la tupla dalla memoria:

del x

