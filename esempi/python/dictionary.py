# DICTIONARY
# sono: composti da coppie chiave-valore, ordinati, non ammettono duplicati di chiave, modificabili

# DICHIARAZIONE:

persona= {
    "nome": "Mario"  ,   # chiave: valore
    "cognome": "Rossi",
    "eta": 20
}

print (persona)

# posso utilizzare TYPE() e LEN():
print(type(persona))
print(len(persona))

# ACCEDERE AI VALORI DEL DICT:
print("il cognome è ", persona["cognome"])

# in alternativa posso utilizzare il metodo get(key):
print( "il cognome è ", persona.get("cognome"))

# posso avere in output solo le chiavi del dictionary.
#utilizzo il metodo keys()

chiavi= persona.keys()
print(chiavi)
print(type(chiavi))

# posso avere in output solo i valori del dictionary.
#utilizzo il metodo values()
valori= persona.values()
print(valori)

# posso stampare le coppie chiave:valore --> si crea una lista si tuple contenti le coppie
#utilizzo il metodo items()
coppie= persona.items()
print(coppie)
print(type(coppie))

# verificare se una chiave è presente nel dict:
print("nome" in persona)

#per modificare gli elementi:
persona["nome"] = "Maria"
print(persona)

#per modificare più elementi utilizzo il metodo update():

persona.update({"nome": "Giovanni", "eta": 30})
print(persona)

# AGGIUNGERE ELEMENTI:
persona["citta"]= "Roma"
print(persona)

#AGGIUNGERE PIù ELEMENTI:
persona.update({"capelli": "biondi", "occhi":"verdi"})
print(persona)

#RIMUOVERE ELEMENTI:

# posso utilizzare pop(key):
persona.pop("capelli")
print(persona)

# posso utilizzare del: 
del persona["occhi"]
print(persona)

# posso utilizzare popitem() per eliminare l'ultimo elemento
persona.popitem()
print(persona)

# posso utilizzare clear() per eliminare tutti gli elementi
# persona.clear()
# print(persona)

# ciclare gli elementi:

for x in persona:
    print(x) # ---> restituisce le chiavi
    
for x in persona:
    print(persona[x]) #--->restituisce i valori

for x in persona.items():
    print(x) # --> restituisce le coppie chiave:valore
    
#COPIARE UN DICTIONARY:

persona2= persona.copy() # --> crea un nuuovo dictionary
print("persona2:",persona2)

# in alternativa posso utilizzare il costruttore:
nuova_persona= dict((persona))
print("nuova_persona:",nuova_persona)

# se vooglio creare due dict dipendenti l'uno dall'altro :
persona2 = persona
print(persona)
print(persona2)

persona["nome"]= "Giovanna"
print("pers:",persona)
print("pers2:",persona2)

# CREARE DICTIONARY ANNIDATI:
animale= {"specie": "gatto", "razza": "persiano", "eta": 2,
          "particolarita": {"occhi": "blu", "pelo": "lungo"}
          }

# accedere ad iun dict annidato:

print(animale["particolarita"]["occhi"])

#ciclo for per dict annidati:

for x in animale["particolarita"].items():
    print(x)

#----------------
for x in animale["particolarita"].keys():
    print(x)

#----------------
for x in animale["particolarita"].values():
    print(x)