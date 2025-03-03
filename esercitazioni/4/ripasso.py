print("-----------------------ESERCIZIO 1------------------------")
var1 = int(input("Inserisci un numero="))
var2 = int(input("Inserisci un numero="))
if var2 < var1:
    print("Il primo numero è maggiore del secondo")
else:
    print("Il secondo numero è maggiore del primo")

print("-----------------------ESERCIZIO 2------------------------")
a = int(input("Inserisci il primo numero="))
b = int(input("Inserisci il secondo numero="))
c = int(input("Inserisci il terzo numero="))

if a>b and a>c:
    print("Il primo numero è maggiore del secondo e del terzo")
elif b>a and b>c:
    print("Il secondo numero è maggiore del primo e del terzo")
elif c>a and c>b:
    print("Il terzo numero è maggiore del primo e del secondo")

print("-----------------------ESERCIZIO 3------------------------")
var3 = [1,2,3,4,5]
varmax = max(var3)
print(var3)

print("-----------------------ESERCIZIO 4------------------------")
var4 = 1
for num in var3:
    var4 *= num
print("Il prodotto tra gli elementi della lista è:",var4)

print("-----------------------ESERCIZIO 5------------------------")
var5 = input("Inserisci un valore=")
if var5 not in var3:
    print("Il valore che hai inserito non è presente nella lista")
else:
    print("Il valore",var5,"è presente nella lista")

print("-----------------------ESERCIZIO 6------------------------")
for var6 in range (1,16):
    print(var6)

print("-----------------------ESERCIZIO 7------------------------")
numeri = []
som7 = 0
avg7 = 1
for i in range(5):
    iNum = int(input(f"Inserisci un numero=({i+1}/5): "))
    numeri.append(iNum)
    som7 += iNum
avg7 = som7/5
print("La somma dei numeri è:", som7)
print("La media dei numeri è:", avg7)