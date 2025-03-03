# per aprire un file usiamo la funzione open() --> ha due parametri: 1) il file al quale vogliamo 
# accedere, 2) la modalità di accesso al file:


#per accedere il lettura, si utilizza il parametro "r" --> read
f= open("prova.txt", "r" )
print(f.read())

#la funzione read() può prendere come parametro un intero, rappresenta il numero di caratteri da leggere
print(f.read(10))

# esiste anche la funzione readline() --> viene utilizzata con testo su più righe:
f= open("prova.txt", "r" )
print(f.readline())

 # se vogliamo leggere tutto con readline() possiamo utilizzare il ciclo for:
f= open("prova.txt", "r" )
for riga in f:
    print(riga)
    
# quando vogliamo cambiare modalità di accesso al file, dobbiamo prima chiudere l'accesso precedente al file
# per fare questo utilizziamo close():
f.close()

# ----- aggiungere del testo al file ----
# si utilizza la funzione open, con parametro "a" --> append

f= open("prova.txt", "a")
f.write("\nciao\na tutti") # \n indica una nuova riga
f.close()

# per vedere le modifiche:
f= open("prova.txt", "r")
print(f.read())
f.close()

# sovrascrivere il testo:
# si utilizza il parametro "w" --> write

f= open("prova.txt", "w")
f.write("testo sovrasxcritto!")
f.close()

# creare un nuovo file.txt :
#possiamo utilizzare il parametro "w" oppure "x"
#differenze: x--> crea un nuovo file se non ne esiste già uno con lo stesso nome
#"w" --> se esiste gia un file con lo stesso nome, lo sovrascrive

f=open("testo.txt", "w")
f.close()

# eliminare un file: dobbiamo importare il modulo os
# os ha la funzione remove()
import os
os.remove("testo.txt")
print("file rimosso")

# se vogliamo controllare se il file esiste prima di eliminarlo:

if os.path.exists("testo.txt"):
    os.remove("testo.txt")
    print("file rimosso")
else:
    print("file non trovato")

# funzione per eliminare cartelle:
#os.rmdir("nome_cartella o path")