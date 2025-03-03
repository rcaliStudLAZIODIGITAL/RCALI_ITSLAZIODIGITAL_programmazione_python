
# programma per lavorare con un file:

# accedo in "creazione" al file:
file= open("mio_file.txt", "w")

# assegno più di una stringa ad una lista:
l= ["Ciao a tutti", "\nquesto è un nuovo file", "\n creato da codice"]

# inserisco una stringa e il contenuto della lista nel file:
file.write("NUOVO FILE:\n")
file.writelines(l)
file.close()

file= open("mio_file.txt", "r")
print(file.read())

# con la funzione seek() spostiamo il cursore all'inizio del file in una posizione specifica
file.seek(0)

print(file.read())

# differenza tra metodo readline() e readlines()
file.seek(0)
print("stampa di readline(): ", file.readline(2))

file.seek(0)
print("stampa di readlines(): ", file.readlines())

print("il puntatore si trova in pos: ",file.tell()) # indica dove si trova il puntatore
file.close()

import os
os.remove("mio_file.txt")