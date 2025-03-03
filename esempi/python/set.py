# SET
# sono: NON ordinati, NON indicizzati, NON modificabili (anche se possiamo eliminare e aggiungere 
# elementi), NON ammettono duplicati
# consentono valori misti!

# DICHIARAZIONE:
x= {"milano", "roma", "bari", "venezia"}
print(x)

#anche pèper i set abbiamo il metodo costruttore:
num = set((1,3,5))
print(num)

# metodo TYPE() 
print(type(x))

#metodo LEN()
print(len(x))

# accedere agli elementi del set:
# non sono indicizzati, quindi non posso usare l'indice numerico, posso vedere gli elementi con un for

for citta in x:
    print(citta)

# verificare se un valore è presente:

if "milano" in x:
    print("presente")
else:
    print("assente")
    
# modo alternativo ( valido anche per liste e tuple)
print("firenze" in x)

# POSSIAMO AGGIUNGERE ELEMENTI:
x.add("Torino")
print(x)

# se provo ad aggiungere un elemento già esistente, il comando viene ignorato
# se cambio anche solo un carattere, l'elemento viene aggiunto
x.add("roma")
print(x)

#POSSIAMO RIMUOVERE GLI ELEMENTI:
x.remove("roma")
print(x)

x.discard("milano")
print(x)

# differenza remove / discard ---> remove da errore se cerchiamo di elimane 
# un elemento non presente nel set ; discard passa oltre (ignora il comando)

#posso eliminare tutti gli elementi del set:
x.clear()
print(x)

#deallocare il set

# del x 
# print(x)
 
# COME UNIRE I SET.

num_pari = {2,4,6,8}
num_dispari={1,3,5,7}

# metodo union() --> crea un nuovo set:
numeri= num_pari.union(num_dispari)
print(numeri)

# metodo update() --> unisce gli elementi di un set in un altro:
num_pari.update(num_dispari)
print(num_pari)

# entrambi i metodi ignorano i duplicati!!

# metodo intesection_update() --> restituisce solo i valori in comune
k= {"cane", "gatto", "coniglio", "volpe"}
j= {"volpe", "cane", "gatto", "rana", "mucca"}

# aggiorno il set k:
k.intersection_update(j)
print("intesection: ", k)

# per creare un nuovo set con i valori in comune tra k e j
# utilizzo il metodo intersection()

animali = k.intersection(j)
print("animali:", animali)

# posso creare un nuovo set con gli elementi univoci dei 2 set:
# utilizzo il metodo symmetric_difference():

cibo= {"pizza", "pasta", "insalata"}
alimenti= {"pizza", "verdure", "pasta"}

c= cibo.symmetric_difference(alimenti)
print(c)

# utilizzo il metodo symmetric_difference_update() per aggiornare un set con i valori univoci
cibo.symmetric_difference_update(alimenti)
print(cibo)
