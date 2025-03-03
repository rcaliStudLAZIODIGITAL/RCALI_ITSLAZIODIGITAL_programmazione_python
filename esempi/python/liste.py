# LISTE --> fanno parte delle collection e sono collezioni di dati
# le liste sono: ordinate, indicizzate, modificabili e ammettono valori duplicati
# le riconosciamo dalle parentesi []

# come dichiarare le liste:

x = ["ciao", 1, 15.2, True] # possono contenere tipi di dato diverso

# METODI PER AVERE INFORMAZIONI SULLA LISTA:

#TYPE() --> serve a vedere il tipo di dato ( list )
# NON indica il tipo di dato degli elementi in lista!!!!

print(type(x)) # <class list>

#LEN() --> restituisce il numero di elementi contenuti nella lista:
print(len(x))

# list() --> metodo costruttore per creare delle liste
num= list((1,2,3,4))
print(num)

# come accedere agli elementi della lista:

print(num[0]) #stampa il primo elemento della lista

print(num[-1]) # stampa l'ultimo elemento della lista

print(num[1:3]) # 3 escluso!

# utilizzo di if per le liste:

y = ["ciao", "buongiorno", "buonasera"]

if "ciao" in y:
    print("elemento presente in lista")
else:
    print("elemento assente!")
    
# MODIFICARE GLI ELEMENTI IN LISTA:

y[0] = "Mario"
print(y)

y[1:3] = [12, 15]
print(y)

# INSERIRE NUOVI ELEMENTI:

#inserire valori in fondo alla lista
y.append(5)
print(y)

#inserire valori in una posizione (indice) specifica:
y.insert(1, "ciao")
print(y)

# inserire valori proventienti da un'altra lista:
z= ["Roma", "Torino"]

y.extend(z)
print("y: ", y)
print("z:" , z)

#RIMUOVERE GLI ELEMENTI DALLA LISTA:

# specifichiamo il valore da rimuovere
y.remove("Torino")
print(y)

# rimuovere l'ultimo elemento della lista
y.pop()
print(y)

# rimuovere un elemento della lista specificando l'indice:
y.pop(0)
print(y)

# svuotare la lista
y.clear()
print(y)

# deallocare la lista ( rimuoverla dalla memoria)

del y 
print(y)