# FUNZIONI --> sono blocchi di codice che possono essere eseguiti a "chiamata" quando necessario

#CREARE UNA FUNZIONE ( dichiarare una funzione)

def prepara_pasta ():
    print("fai bollire l'acqua")
    print("metti la pasta nell'acqua bollente")
    print("scola la pasta e condisci")
    print("impiatta e mangia")

    
# INVOCARE LA FUNZIONE:
prepara_pasta() # possiamo invocarla quante volte vogliamo!


# parametri di funzione:
def somma(num1, num2):
    totale= num1+num2
    print("risulatato somma:",totale)
    
somma(1,2)
somma(10,20)

# in alternativa --> invocazione con key arguments
somma(num1=5, num2=7)

# uso dei parametri di default:

def somma_2(num1=5, num2=3):
    tot= num1+num2
    print(tot)
    
#invoco la funzione senza dare valore ai parametri:
somma_2()

#invoco la funzione dando valore ai parametri:
somma_2(4,6)

#COMANDO RETURN:

def somma_3(num1, num2):
    somma= num1+num2
    return somma # quando viene invocata la funzione, questa restituisce il valore di somma

# memorizzo in x il risultato della chiamata a somma_3():
x= somma_3(3,3)

# utilizzo x come voglio:
print(x)
print(x+5)

# SCOPE DELLE VARIABILI:

# SCOPE LOCALE --> variabili definite nelle funzioni:

def funzione_1():
    variabile_locale= 800
    print(variabile_locale)
    
funzione_1()
# print(variabile_locale) ---> restituisce errore!!!

# SCOPE GLOBALE --> variabili dichiarate fuori dalle funzioni ma che possono essere usate nelle funzioni

n1= 300
n2= 200

def sottrazione():
    risul = n1-n2
    return risul

print(sottrazione())

# PAROLA CHIAVE GLOBAL: serve a trasformare una variabile locale in globale

n3= 200
n4= 400
risultato= n4+n3
print("risultato fuori dalla funzione: ", risultato)

def sottrazione_2():
    global risultato # dichiro la variabile risultato come variabile globale
    risultato= n3-n4
    return risultato

print(risultato)

print(sottrazione_2())
print("risultato dopo la chiamata alla funzione: ", risultato)

# FUNZIONI LAMBDA
# sono funzioni semplici con sintassi abbreviata

#sintassi per la dichiarazione di una Lambda: nome = lambda parametri : valore restituito
# esempio: voglio creare una lambda per la somma: 

addiz= lambda a,b : a+b

# equivale a:
# def addiz(a,b):
#     tot= a+b
#     return tot

#INVOCARE UNA FUNZIONE LAMBDA: 
print(addiz(3,5)) # allo stesso modo delle funzioni classiche!

# sono utili perchè possono essere utilizzate come parametri nell'invocazione di altre funzioni
#in questo caso si definiscono come funzioni anonime , quindi, senza nome

lista= ["albero", "cane", "gatto", "acqua"]

# esempio: voglio una nuova lista con i soli valori di <lista> che cominciano con la lettera a

# potrei gestire il problema con il for:

nuova=[]

for x in lista:
    if x.startswith("a"):
        nuova.append(x)
    
print("nuova lista", nuova)

# in alternativa, posso utilizzare la funzione built-in filter()
# filter(funzione, collection) --> seleziona gli elementi di una collection in base al risultato di una funzione

nuova2= list(filter(lambda x: x.startswith("a"), lista))
print("nuova lista2", nuova2)

# FUNZIONE MAP(funzione, collection)
# esempio: data una lista di numeri, voglio applicare ad ogni elemento la funzone che ritorna il quadrato

numeri= [1,2,3,4]

quadrato_numeri=list(map(lambda n: n**2, numeri))

print(quadrato_numeri)