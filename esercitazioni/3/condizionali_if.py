var=10
print("-----------------------ESERCIZIO 1------------------------")
iNum = int(input("Inserisci un numero="))
if iNum >= 0:
    print("Il numero è positivo")
else:
    print("Il numero è negativo")
print("il numero che hai inserito è:",type(iNum),iNum)

print("-----------------------ESERCIZIO 2------------------------")
iNum1 = int(input("Inserisci un numero="))
iNum2 = int(input("Inserisci un numero="))
if iNum2 < iNum1:
    print("Il primo numero è maggiore del secondo")
else:
    print("Il secondo numero è maggiore del primo")

print("-----------------------ESERCIZIO 3------------------------")
iStr=str(input("Inserisci una stringa="))
if len(iStr) == 0:
    print("La stringa inserita è vuota")
else:
    print("La stringa inserita non è vuota")

print("-----------------------ESERCIZIO 4------------------------")
iNumX=int(input("Inserisci il numero="))
if iNumX % 2 == 0:
    print("Il numero inserito è pari")
else:
    print("Il numero inserito è dispari")

print("-----------------------ESERCIZIO 5------------------------")
iChar=str(input("Inserisci una lettera="))
if iChar not in ("aeiou"):
    print("La lettera è una consonante")
else:
    print("La lettera è una vocale")

print("-----------------------ESERCIZIO 6------------------------")
iNumY=int(input("Inserisci un numero="))
if iNumY<10 and iNumY>1:
    print("Il numero inserito è compreso tra 1 e 10")
else:
    print("Il numero inserito non è compreso tra 1 e 10")

print("-----------------------ESERCIZIO 7------------------------")
iNumZ=int(input("Inserisci un numero intero="))
if iNumZ > 10:
    print("Il numero inserito è maggiore di 10")
elif iNumZ < 10:
    print("Il numero inserito è minore di 10")
elif iNumZ == 10:
    print("Complimenti, hai inserito 10,","per la tua pazienza ecco il tuo voto:",var)