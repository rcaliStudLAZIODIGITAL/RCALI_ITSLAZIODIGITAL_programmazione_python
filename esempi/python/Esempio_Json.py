# SCRIVERE UN FILE JSON:

import json

#dati da inserire:
cliente= {"nome": "Mario", "cognome": "Rossi", "eta":25, "nuovo_cliente": True, 
         "aricoli": ["iphone", "samsung galaxy 15", "cover blu"], "tot_spesa": 895.78}

nuovo= open("test.json", "w")

#utillo dump() per inserire cliente nel nuovo file:
# dump() ha due parametri : contenuto da inserire nel file, variabile di accesso al file:

json.dump(cliente, nuovo)
nuovo.close()

#----- ACCEDO IN LETTURA -----

f= open("test.json","r")

dati= json.load(f)

print(dati)

f.close()

#------ AGGIORNO IL JSON -----

file= open("test.json", "r+") 
# "r+" ---> accesso sia in lettura che in scrittura

dati= json.load(file)# trasformo il contenuto del file in un dict

# dichiaro cosa devo aggiungere:

aggiunta= {"email": "m.rossi@email.it", "password": "abc123"}

dati.update(aggiunta)
print(dati)

# riposiziono il cursone all'inizio del file:
file.seek(0)

#inserisco tutto nel file:

json.dump(dati, file)

file.close()