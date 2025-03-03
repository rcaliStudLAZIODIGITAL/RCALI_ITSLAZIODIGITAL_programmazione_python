print("-----------------------ESERCIZIO 1------------------------")
a = lambda x:x**2
print("Risultato lambda A:",a(5))

print("-----------------------ESERCIZIO 2------------------------")
listaB1 = [1,2,3,4,5]
listaB2 = list(map(lambda x:x*2,listaB1))
print("Risultato lambda B:",listaB2)

print("-----------------------ESERCIZIO 3------------------------")
listaC1 = ["albero", "cane", "gatto", "acqua"]
c = list(filter(lambda x:x.startswith("c"),listaC1))
print("Risultato lambda C:",c)

print("-----------------------ESERCIZIO 4------------------------")
d = lambda a, b:(a**2)+(b**2)
print("Risultato lambda D:",d(5,6))