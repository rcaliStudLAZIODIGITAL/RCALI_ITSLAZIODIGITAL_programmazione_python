# Json (javascript object notation) --> formato leggero per salvare a trasportate i dati

# dobbiamo importare il modulo json:

import json

#creo una stringa json:
x= '{"nome": "Mario", "cognome": "Rossi", "eta":25}'

# per trasformare una stringa json in un dict utilizzo la funzione loads()

y= json.loads(x)
print(y)
print(type(y))

# per convertire un dict in Json, utilizzo dumps()

j= json.dumps(y)
print(type(j))

#quali altri tipi di dato posso convertire?

# list:
print(json.dumps(["mela", "pera", "pesca"]))

#tuple:
print(json.dumps(("mela", "pera", "pesca")))

#stringhe:
print(json.dumps("mela"))

# int, float, Bool

utente= {"nome": "Mario", "cognome": "Rossi", "eta":25, "nuovo_cliente": True, 
         "aricoli": ["iphone", "samsung galaxy 15", "cover blu"], "tot_spesa": 895.78}

# dumps() accetta anche dei parametri:
# parametro indent= n ---> indenta le coppie chiave/valore
print(json.dumps(utente, indent=4))

#parametro separators --> modifica il separatore chiave/valore
#primo parametro --> separatore delle coppie chiave/valore , 
#secondo parametro --> separatore tra chiave e valore

print(json.dumps(utente, indent=4, separators=(",","=")))

#parametro sort_keys=  --> seve a ordinare le chiavi in modo crescente:
print(json.dumps(utente, indent=4, separators=(",","="), sort_keys=True))

