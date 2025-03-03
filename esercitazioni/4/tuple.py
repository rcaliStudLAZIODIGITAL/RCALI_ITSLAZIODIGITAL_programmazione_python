print("-----------------------ESERCIZIO 1------------------------")
tupla = ("mela","pera","arancia")
print(tupla)

print("-----------------------ESERCIZIO 2------------------------")
var1 = tuple(("pesca", "banana", "kiwi"))
print(var1)
var2 = tuple((1,2,3,4))+var1+tupla
print(var2)

print("-----------------------ESERCIZIO 3------------------------")
print(type(var2[6]),var2[6])

print("-----------------------ESERCIZIO 4------------------------")
print("Ecco i primi 2 elementi:",var2[0:2])

print("-----------------------ESERCIZIO 5------------------------")
if "ananas" in var2 :
    print("ananas presente")
else:
    print("ananas assente")

print("-----------------------ESERCIZIO 6------------------------")
print(len(var2))

print("-----------------------ESERCIZIO 7------------------------")
print("es2")

print("-----------------------ESERCIZIO 8------------------------")
nMela= var2.count("mela")
print("il valore è ripetuto",nMela,"volta/e")