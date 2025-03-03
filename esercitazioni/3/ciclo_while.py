print("-----------------------ESERCIZIO 1------------------------")
var = 0
while var<10:
    var+=1
    print(var)

print("-----------------------ESERCIZIO 2------------------------")
# n=0 #Hack
n = int(input("Inserisci un numero="))
var = 1
while var<n:
    var+=var
    print(var)

print("-----------------------ESERCIZIO 3------------------------")
var = 2
while var<10:
    if var%2==0:
        ris3 = var
        print(ris3)
    var+=1

print("-----------------------ESERCIZIO 4------------------------")
import random
ran4 = random.randint(1,10)
# print(ran4) #Hack view rand
# num = ran4 #Hack
num = int(input("Inserisci un numero tra 1 e 10="))
while True:
    if num == ran4:
        print("Daje!")
        break
    else:
        num = int(input("Non daje! Riprova="))

print("-----------------------ESERCIZIO 5------------------------")
# string = "" #Hack
string = input("Dimmi qualcosa...")
i=len(string)-1
while i>=0:
    print(string[i])
    i-=1

print("-----------------------ESERCIZIO 6------------------------")
i=10
while i>=1:
    print(i)
    i-=1

print("-----------------------ESERCIZIO 7------------------------")
# i=0 #Hack
i = int(input("Inserisci un numero intero:"))
fatto = i
while i > 1:
    fatto *= i
    i-=1
print("Il fattoriale è:",fatto)

print("-----------------------ESERCIZIO 8------------------------")
i = 0
somma = 0
# j = 0 #Hack
j = int(input("Quanti numeri vuoi inserire?"))
while i < j:
    print("Numero",i+1)
    iNum = int(input())
    somma += iNum
    i+=1
print("La somma è:",somma)

print("-----------------------ESERCIZIO 9------------------------")
# string = "" #Hack
string = input("Dimmi qualcosa...")
i=0
cnv9 = ""
con9 = ""
consonanti = "qwrtypsdfghjklzxcvbnmçQWRTYPSDFGHJKLZXCVBNM"
vocali = "aeiouAEIOUàèéìòù"
while i<len(string):
    char = string[i]
    if char not in vocali and char not in consonanti:
        cnv9 += char + " "
    if char in consonanti:
        con9 += char + " "
    i+=1
print("Caratteri non alfabetici:",cnv9)
print("Consonanti:",con9)