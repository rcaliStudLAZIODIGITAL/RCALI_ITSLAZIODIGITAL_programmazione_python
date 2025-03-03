
# COSTRUTTO IF SEMPLICE:

x= 15

if x<10 : 
    print("x è minore di 10!") #attenzione all'indentazione!



#operatori di comparazione:

x=5

# == --> uguale a..
if x==5 : 
    print("x è uguale a 5")

# != --> diverso da..

if x != 5 : 
    print(" x è diverso da 5")


# compreso tra ( range )

x= 10

if x in range (0,15):
    print( "x è compreso tra 0 e 15")
    
# OPERATORI LOGICI:

x= 11
y= 20

# AND ( e ) --> entrambe le condizioni devono restituire true

if x>10 and y>10:
    print("condizione And verificata!!")
    
# OR (oppure) --> una o entrambe le condizioni restituiscono true

if x>10 or y<20:
    print("condizione or verificata!!")

# NOT --> se la condizione restituisce true il not fa si che l'if restituisca false e viceversa

if not(x==11) : 
    print("x è uguale a 11")
    
    
# costrutto IF ... ELSE 

z= 25

if z == 15: 
    print("z è uguale a 15")

else:
    print("z è diverso da 15")  # viene eseguito solo se la condizione restituisce false


# costrutto IF...ELIF...ELSE

k= 20

if k ==10:
    print("k è uguale a 10")
elif k == 15:
     print("k è uguale a 15")
elif k == 18:
    print("k è uguale a 18")
else :
    print("k non è uguale a 10, 15 o 18")
    

# IF ANNIDATI:
# esempio: voglio chiedere un numero da terminale e controllare se è paro e maggiore di 10:

num= int(input("scrivi un numero: "))

if num % 2 == 0:  
    print("il numero che hai scritto è un numero paro")
    if num>10 :
        print("il numero che hai scritto è anche maggiore di 10")
    else:
        print("il numero che hai scritto è minore di 10")
else:
    print("il numero che hai scritto è disparo")
