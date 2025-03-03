print("-----------------------ESERCIZIO 1------------------------")
persona = {}
print(persona)

print("-----------------------ESERCIZIO 2------------------------")
persona = {
    "nome": "Mario",
    "cognome": "Rossi",
    "eta": 30
} 
print(persona)

print("-----------------------ESERCIZIO 3------------------------")
print(persona["eta"])

print("-----------------------ESERCIZIO 4------------------------")
persona["email"]="mario.rossi@mail.com"
print(persona)

print("-----------------------ESERCIZIO 5------------------------")
persona.pop("cognome")
print(persona)

print("-----------------------ESERCIZIO 6------------------------")
print(persona.keys())

print("-----------------------ESERCIZIO 7------------------------")
print(persona.values())

print("-----------------------ESERCIZIO 8------------------------")
persona["eta"]=35
print(persona)

print("-----------------------ESERCIZIO 9------------------------")
print("Il numero di elementi nel dizionario è:",len(persona))