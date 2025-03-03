# CLICLO WHILE
# si utilizza per far compiere automaticamente un'azione al programma finchè la condizione restituisce true

#Esempio: chiedere all'utente un numero, 
#stampare il numero inserito fintanto che viene inserito un numero minore di 6

x= int(input("scrivi un numero: "))

while x < 6:
    print(x)
    x=int(input("scrivi altro numero: "))

print("ciclo while interrotto!")

# Esempio con autoincremento di variabile:
# voglio stampare nel terminale i numeri da 1 a 10

num = 1

while num <=10 : 
    print(num)
    num+=1
    
print("ciclo while interrotto!")

#COMANDO BREAK --> serve ad interrompere il ciclo

y=0

while y<=10:
    print(y)
    
    if y==5:
        break
    
    y+=1
    
print("ciclo while interrotto!")    


# CONTINUE --> salta un'iterazione
z= 0
while z<10:
    z+=1
    if z == 5:
        continue
    print(z)

print("ciclo while interrotto!")    
print(z)

# ELSE:

k= 0
while k<=10:
    print(k)
    k+=1
else:
    print("ciclo while finito!") 